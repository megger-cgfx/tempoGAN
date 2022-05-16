import os
import subprocess



# for sim in range(1002,1003):
#     for frame in range(0,201,10):
#         print(f"\n\nSim: {sim}\nFrame: {frame}\n\n")
#         logfile = f"{logdir}/log_{frame:04}.txt"
#         with open(logfile, "w") as logfile:
#             subprocess.run(
#                 f"python tempoGAN.py fromSim {sim} frameMin {frame} logfile {logfile}.txt", shell=True,
#                 stdout=logfile
#             )


# for sim in range(1000,1003):
#     for frame in range(0,201):
#
#         outfile = f"C:\\Work\\22-04_multipassGAN\\3ddata_sim_arbitraryshape\\sim_{sim}\\density_superres_{frame:04}.npz"
#         if not os.path.exists(outfile):  # Only run for non-existing frames
#
#             print(f"\n\nSim: {sim}\nFrame: {frame}\n\n")
#
#             logdir = f"/mnt/c/Work/22-04_multipassGAN/3ddata_sim_arbitraryshape/sim_{sim}/logs"
#             #logdir = f"C:\\Work\\22-04_multipassGAN\\3ddata_sim_arbitraryshape\\sim_{sim}\\logs"
#             if not os.path.exists(logdir):
#                 os.mkdir(logdir)
#             logfile = os.path.join(logdir, f"log_{frame:04}.txt")
#             #with open(logfile, "w") as logfile:
#             subprocess.run(
#                 f"python tempoGAN.py fromSim {sim} frameMin {frame} > {logfile}.txt", shell=True
#             )


for sim in range(1000,1003):
    for frame in range(15,201):

        outfile = f"/mnt/c/Work/22-04_multipassGAN/3ddata_sim_arbitraryshape/sim_{sim}/density_superres_{frame:04}.npz"
        if not os.path.exists(outfile):  # Only run for non-existing frames

            print(f"\n\nSim: {sim}\nFrame: {frame}\n\n")

            logdir = f"/mnt/c/Work/22-04_multipassGAN/3ddata_sim_arbitraryshape/sim_{sim}/logs"
            if not os.path.exists(logdir):
                os.mkdir(logdir)
            logfile = f"{logdir}/log_{frame:04}.txt"

            with open(logfile, "w") as logfile:
                subprocess.run(
                    f"python tempoGAN.py fromSim {sim} frame {frame}", shell=True,
                    stdout=logfile
                )