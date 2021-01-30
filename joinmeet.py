import argparse
from utils.attender import Attender


parser = argparse.ArgumentParser(description='Auto Attender System')
parser.add_argument('-m', '--meetcode',
                    type=str, help='meetcode to join', required=True)
args = parser.parse_args()

attend = Attender(block_chrome_mic_camera=False, mute_chrome_audio=False)
attend.join_meet(args.meetcode)
