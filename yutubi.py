import os
import argparse
import subprocess

from pytube import YouTube

def run():
    zelda = YouTube(target_url)
    dl = zelda.streams.get_highest_resolution()
    return dl


def download():
    video_dl_path = os.path.join(target_dir, default_filename)

    if os.path.exists(video_dl_path):
        #remove duplicates
        os.remove(video_dl_path)
    
    os.chdir(target_dir)
    video.download()
    
    os.chdir("../")
    return video_dl_path


def convert_output():
    audio_dl_path = os.path.join(currentdir, "audio_downloads")

    if not os.path.exists(audio_dl_path):
        os.mkdir(audio_dl_path)

    output_filename = os.path.join(audio_dl_path, new_filename)
    
    #Brief explanation of the following lines: instead of "hardcoding" output bitrate, should check what the video's audio track bitrate is
    #curretly this seems to be retrieving ~127kbps, need more research into this topic so for now just hardcoding bitrate conversion at 320 (probably bad idea)
    #result = subprocess.run(['ffprobe', '-v', 'quiet', '-select_streams', 'a:0', '-show_entries', 'stream=bit_rate', '-of', 'default=noprint_wrappers=1', video_dl_path], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    #print(result)
    
    subprocess.call([
            'ffmpeg', '-i', video_dl_path, "-b:a", "320k", output_filename
        ])
    
    if not keep_video:
        os.remove(video_dl_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", type=str, help="Url of the video to download", required=True)
    parser.add_argument("-a", "--audio", help="Add this flag if wish to convert the video to audio", action="store_true")
    parser.add_argument("-v", "--video", help="Add this flag only when converting to audio if you wish to keep the video", action="store_true")

    args = parser.parse_args()

    target_url = args.url
    convert_audio = args.audio
    
    if convert_audio:
        keep_video = args.video

    video = run()
    default_filename = video.default_filename
    
    currentdir = os.getcwd()
    target_dir = os.path.join(currentdir, "video_downloads")

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)


    video_dl_path = download()

    if convert_audio:
        new_filename = video.default_filename.replace(".", "").replace(" ", "_")[:-3] + ".mp3"
        convert_output()
    