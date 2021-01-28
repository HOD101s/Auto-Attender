import argparse
from utils.scheduler import Scheduler


parser = argparse.ArgumentParser(description='Auto Attender System')
parser.add_argument('-build-sc', '--build_schedule',
                    default=True, type=bool, help='run schedule builder')
args = parser.parse_args()


scheduler = Scheduler(launch_interval=20, build_schedule=args.build_schedule,
                      block_mic_cam=False, mute_audio=False)
scheduler.attendLecture()
