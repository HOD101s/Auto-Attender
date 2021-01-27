import argparse
from utils.attender import Attender


parser = argparse.ArgumentParser(description='Auto Attender System')
parser.add_argument('-c', '--meetcode',
                    type=str, help='meetcode to join', required=True)
args = parser.parse_args()

attend = Attender(block_mic_cam=False, mute_audio=False)
attend.join_meet(args.meetcode)
