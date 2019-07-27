import pyaudio as pa
import time
import numpy as np
import soundfile as sf
import sys
import scipy.signal as sg
import matplotlib.pyplot as plt

xs = np.array([])


def find_peaks(a, amp_thre, local_width=1, min_peak_distance=1):
    """
    閾値と極大・極小を判定する窓幅、ピーク間最小距離を与えて配列からピークを検出する。
    内部的にはピーク間距離は正負で区別して算出されるため、近接した正負のピークは検出される。
    :rtype (int, float)
    :return tuple (ndarray of peak indices, ndarray of peak value)
    """
    # generate candidate indices to limit by threthold
    idxs = np.where(np.abs(a) > amp_thre)[0]

    # extend array to decide local maxima/minimum
    idxs_with_offset = idxs + local_width
    a_extend = np.r_[[a[0]] * local_width, a, [a[-1]] * local_width]

    last_pos_peak_idx = 0
    last_neg_peak_idx = 0
    result_idxs = []

    for i in idxs_with_offset:
        is_local_maximum = (a_extend[i] >= 0 and
                            a_extend[i] >= np.max(a_extend[i - local_width: i + local_width + 1]))
        is_local_minimum = (a_extend[i] < 0 and
                            a_extend[i] <= np.min(a_extend[i - local_width: i + local_width + 1]))
        if (is_local_maximum or is_local_minimum):
            if is_local_minimum:
                if i - last_pos_peak_idx > min_peak_distance:
                    result_idxs.append(i)
                    last_pos_peak_idx = i
            else:
                if i - last_neg_peak_idx > min_peak_distance:
                    result_idxs.append(i)
                    last_neg_peak_idx = i

    result_idxs = np.array(result_idxs) - local_width
    return (result_idxs, a[result_idxs])


def callback(in_data, frame_count, time_info, status):
    global xs
    in_float = np.frombuffer(in_data, dtype=np.int16).astype(np.float)
    in_float[in_float > 0.0] /= float(2 ** 15 - 1)
    in_float[in_float <= 0.0] /= float(2 ** 15)
    xs = np.r_[xs, in_float]

    return (in_data, pa.paContinue)


if __name__ == "__main__":
    # pyaudio
    p_in = pa.PyAudio()
    py_format = p_in.get_format_from_width(2)
    fs = 16000
    channels = 1
    chunk = 1024
    use_device_index = 0

    # 入力ストリームを作成
    in_stream = p_in.open(format=py_format,
                          channels=channels,
                          rate=fs,
                          input=True,
                          frames_per_buffer=chunk,
                          input_device_index=use_device_index,
                          stream_callback=callback)

    in_stream.start_stream()

    # input loop
    # 何か入力したら終了
    while in_stream.is_active():
        c = input()
        if c:
            break
        time.sleep(0.1)
    else:
        in_stream.stop_stream()
        in_stream.close()

    # 入力信号を保存
    sf.write("pyaudio_output.wav", xs, fs)

    p_in.terminate()

    # デジタルフィルタを時系列信号に適用する
    plt.close("all")

    # wavファイル読み込み
    filename = sys.argv[1]
    wav, fs = sf.read(filename)

    # # ステレオ2chの場合、LchとRchに分割
    # wav_l = wav[:, 0]
    # wav_r = wav[:, 1]

    # 入力をモノラル化
    # xs = (0.5 * wav_l) + (0.5 * wav_r)
    xs = wav

    aaa, bbb = find_peaks(xs, 256)

    # LPF設計
    num_tap = 1024
    lpf_cutoff_hz = 400.0
    lpf_cutoff = lpf_cutoff_hz / (fs / 2.0)
    win = "hann"
    lpf = sg.firwin(num_tap, lpf_cutoff, window=win)

    # 線形フィルタ適用
    ys = sg.lfilter(lpf, [1.0], xs)

    # 周波数領域フィルタ適用
    zs = sg.fftconvolve(xs, lpf, mode="same")

    # 冒頭から10秒分プロット
    fig = plt.figure(1)
    ax = fig.add_subplot(311)
    ax.plot(xs[:fs * 10])
    ax.set_title("input signal")
    ax.set_xlabel("time [pt]")
    ax.set_ylabel("amplitude")

    ax = fig.add_subplot(312)
    ax.plot(ys[:fs * 10])
    ax.set_title("lfilter output signal")
    ax.set_xlabel("time [pt]")
    ax.set_ylabel("amplitude")

    ax = fig.add_subplot(313)
    ax.plot(ys[:fs * 10])
    ax.set_title("fftconvolve output signal")
    ax.set_xlabel("time [pt]")
    ax.set_ylabel("amplitude")

    fig.set_tight_layout(True)

    plt.show()
