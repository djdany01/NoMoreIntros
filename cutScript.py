from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.video.io.VideoFileClip import VideoFileClip
import os, psutil, time


def check_list(file_list):
    if not file_list:
        return False
    else:
        return True


def cut_video(begin, end, file_list):

    c = 0

    for i in file_list:
        try:
            video = VideoFileClip(i.path)
        except Exception as e:
            continue
        ffmpeg_extract_subclip(
            i.path.replace('\\', '/'), int(begin), video.duration-int(end), targetname=i.path.replace('\\', '/')[:-4]+'n'+i.path[len(i.path)-4:])

        video.reader.close()
        video.audio.reader.close_proc()
        video.close()

        c = c+1

    return {'state': True, 'num': str(c)}


def delete_files(files_delete):
    kill_ffmpeg()
    time.sleep(0.5)
    for i in files_delete:
        try:
            os.remove(i.path)
        except:
            return False
    return True


def kill_ffmpeg():
    for proc in psutil.process_iter():
        if 'ffmpeg' in proc.name():
            print(proc.name)
            proc.kill()