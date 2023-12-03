import os
import glob as gb


data_path = "/home/hydra/modet/usyd-oclr/flow/DAVIS-data/DAVIS"
rgb_path = data_path + "/JPEGImages/480p"
# '/JPEGImages/480p' for DAVIS16 & DAVIS17-motion and '/JPEGImages' for others

gap = [1]
# reverse = [0, 1]
reverse = [1]
batch_size = 4
# folder = gb.glob(os.path.join(rgb_path, "*"))
folder = [
    # "bear",
    # "bmx-bumps",
    "boat",
    "breakdance-flare",
    "bus",
    "car-turn",
    "dance-jump",
    "dog-agility",
    "drift-turn",
    "elephant",
    "flamingo",
    "hike",
    "hockey",
    "horsejump-low",
    "kite-walk",
    "lucia",
    "mallard-fly",
    # "mallard-water",
    # "motocross-bumps",
    # "motorbike",
    # "paragliding",
    # "rhino",
    # "rollerblade",
    # "scooter-gray",
    # "soccerball",
    # "stroller",
    # "surf",
    # "swing",
    # "tennis",
    # "train",
    # "dog",
    # "cows",
    # "goat",
    # "camel",
    # "libby",
    # "parkour",
    # "soapbox",
    # "blackswan",
    # "bmx-trees",
    # "kite-surf",
    # "car-shadow",
    # "breakdance",
    # "dance-twirl",
    # "scooter-black",
    # "drift-chicane",
    # "motocross-jump",
    # "horsejump-high",
    # "drift-straight",
    # "car-roundabout",
    # "paragliding-launch",
]
print(folder)
for r in reverse:
    for g in gap:
        for f in folder:
            print("===> Runing {}, gap {}".format(f, g))
            mode = "raft-things.pth"  # model
            if r == 1:
                raw_outroot = data_path + "/Flows_gap-{}/".format(
                    g
                )  # where to raw flow
                outroot = data_path + "/FlowImages_gap-{}/".format(
                    g
                )  # where to save the image flow
            elif r == 0:
                raw_outroot = data_path + "/Flows_gap{}/".format(g)  # where to raw flow
                outroot = data_path + "/FlowImages_gap{}/".format(
                    g
                )  # where to save the image flow
            f = rgb_path + "/" + f
            print(
                "python predict.py "
                "--gap {} --mode {} --path {} --batch_size {} "
                "--outroot {} --reverse {} --raw_outroot {}".format(
                    g, mode, f, batch_size, outroot, r, raw_outroot
                )
            )
            os.system(
                "python predict.py "
                "--gap {} --mode {} --path {} --batch_size {} "
                "--outroot {} --reverse {} --raw_outroot {}".format(
                    g, mode, f, batch_size, outroot, r, raw_outroot
                )
            )
