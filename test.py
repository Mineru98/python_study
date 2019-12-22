import glob
print(sorted(glob.glob("tmp/*cpu.csv"), reverse=False))
print(sorted(glob.glob("tmp/*cpu.csv"), reverse=True))