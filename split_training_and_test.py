import os
from shutil import copy, rmtree

def mk_file(file_path):
    if os.path.exists(file_path):
        rmtree(file_path)

    os.makedirs(file_path)

def main():
    #get dataset path
    source_path = "C:/Users/75264/Desktop/project module/code/processed"
    pcd_path = "C:/Users/75264/Desktop/project module/code/processed/point_clouds"

    #create folder for the dataset
    train_root = os.path.join(source_path, 'train_dataset')
    mk_file(train_root)

    test_root = os.path.join(source_path, 'test_dataset')
    mk_file(test_root)

    pcd_files = [f for f in os.listdir(pcd_path) if f.endswith('.pcd')]

    pcd_files.sort()

    split_ratio = 0.2
    total = len(pcd_files)
    test_size = int(split_ratio * total)
    train_size = total - test_size

    train_files = pcd_files[:train_size]
    test_files = pcd_files[-test_size:]

    for idx, f in enumerate(train_files):
        copy(os.path.join(pcd_path, f), os.path.join(train_root, f))
        percent = (idx + 1) / len(train_files) * 100
        print("\rCopying train dataset {:.2f}% ({}/{}) - {}".format(percent, idx + 1, len(train_files), f), end="")


    print()
    
    for idx, f in enumerate(test_files):
        copy(os.path.join(pcd_path, f), os.path.join(test_root, f))
        percent  = (idx + 1) / len(test_files) * 100
        print("\rCopying test dataset {:.2f}% ({}/{}) - {}".format(percent, idx + 1, len(test_files), f), end="")


    print("\nProcessing done!")



if __name__ == '__main__':
    main()
