import h5py
import os

file_path = '/Users/xifeng/Documents/个人内容/semg_dataset/emg2pose_dataset_mini/2022-12-06-1670313600-e3096-cv-emg-pose-train@2-recording-9_right.hdf5'

# 检查文件是否存在
if os.path.exists(file_path):
    print("文件存在！")
else:
    print("文件不存在！")

# 检查目录是否存在
directory = os.path.dirname(file_path)
if os.path.exists(directory):
    print(f"目录存在: {directory}")
else:
    print(f"目录不存在: {directory}")


# 打开文件
_file = h5py.File(file_path, "r")
emg2pose_group: h5py.Group = _file["emg2pose"]

# ``timeseries`` is a HDF5 compound Dataset
timeseries: h5py.Dataset = emg2pose_group["timeseries"]
assert timeseries.dtype.fields is not None
assert "emg" in timeseries.dtype.fields
assert "joint_angles" in timeseries.dtype.fields
assert "time" in timeseries.dtype.fields

# Load the metadata entirely into memory as it's rather small
# metadata: dict[str, Any] = {}
for key, val in emg2pose_group.attrs.items():
    print(1)
    # metadata[key] = val
print(1)