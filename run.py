import argparse
from utils.scheduler import Scheduler


def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')


parser = argparse.ArgumentParser(description='Auto Attender System')
parser.add_argument('-l', '--launch_interval',
                    default=20, nargs='?', const=True, type=int, help='Interval to keep checking for current available session')
parser.add_argument('-sc', '--build_schedule', type=str2bool,
                    default=True, nargs='?', const=True, help='Re-builds schedule before attending sessions')
parser.add_argument('-mic', '--block_mic_camera', type=str2bool,
                    default=False, nargs='?', const=True, help='Block Chrome access to Mic and Camera. If set user cannot manually give access to camera or mic')
parser.add_argument('-mute', '--mute_chrome_audio', type=str2bool,
                    default=False, nargs='?', const=True, help='Mutes all audio from the Chrome window. If set user cannot manually un-mute')
args = parser.parse_args()


scheduler = Scheduler(launch_interval=args.launch_interval, build_schedule=args.build_schedule,
                      block_mic_cam=args.block_mic_camera, mute_audio=args.mute_chrome_audio)
scheduler.attendLecture()
