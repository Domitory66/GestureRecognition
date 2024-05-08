import os, shutil
from glob import glob

original_dataset_dir = '/media/deim/Data/Универ/Магистратура/МИН/DiplomaProject/OpenCV/dataset/hagrid_dataset_512'

original_dataset_dir_call = os.path.join(original_dataset_dir,'call')
original_dataset_dir_dislike = os.path.join(original_dataset_dir,'dislike')
original_dataset_dir_fist = os.path.join(original_dataset_dir,'fist')
original_dataset_dir_four = os.path.join(original_dataset_dir,'four')
original_dataset_dir_like = os.path.join(original_dataset_dir,'like')
original_dataset_dir_mute = os.path.join(original_dataset_dir,'mute')
original_dataset_dir_ok = os.path.join(original_dataset_dir,'ok')
original_dataset_dir_one = os.path.join(original_dataset_dir,'one')
original_dataset_dir_palm = os.path.join(original_dataset_dir,'palm')
original_dataset_dir_peace = os.path.join(original_dataset_dir,'peace')
original_dataset_dir_peace_invert = os.path.join(original_dataset_dir,'peace_inverted')
original_dataset_dir_rock = os.path.join(original_dataset_dir,'rock')
original_dataset_dir_stop = os.path.join(original_dataset_dir,'stop')
original_dataset_dir_stop_invert = os.path.join(original_dataset_dir,'stop_inverted')
original_dataset_dir_three = os.path.join(original_dataset_dir,'three')
original_dataset_dir_three2 = os.path.join(original_dataset_dir,'three2')
original_dataset_dir_two_up = os.path.join(original_dataset_dir,'two_up')
original_dataset_dir_two_up_invert = os.path.join(original_dataset_dir,'two_up_inverted')

base_dir = './dataset'
os.mkdir(base_dir)
train_dir= os.path.join(base_dir,'train')
os.mkdir(train_dir)
test_dir=os.path.join(base_dir,'test')
os.mkdir(test_dir)
valid_dir=os.path.join(base_dir,'valid')
os.mkdir(valid_dir)


train_call_dir = os.path.join(train_dir,'call')
os.mkdir(train_call_dir)
train_dislike_dir = os.path.join(train_dir,'dislike')
os.mkdir(train_dislike_dir)
train_fist_dir = os.path.join(train_dir,'fist')
os.mkdir(train_fist_dir)
train_four_dir = os.path.join(train_dir,'four')
os.mkdir(train_four_dir)
train_like_dir = os.path.join(train_dir,'like')
os.mkdir(train_like_dir)
train_mute_dir = os.path.join(train_dir,'mute')
os.mkdir(train_mute_dir)
train_ok_dir = os.path.join(train_dir,'ok')
os.mkdir(train_ok_dir)
train_one_dir = os.path.join(train_dir,'one')
os.mkdir(train_one_dir)
train_palm_dir = os.path.join(train_dir,'palm')
os.mkdir(train_palm_dir)
train_peace_dir = os.path.join(train_dir,'peace')
os.mkdir(train_peace_dir)
train_peace_invert_dir = os.path.join(train_dir,'peace_invert')
os.mkdir(train_peace_invert_dir)
train_rock_dir = os.path.join(train_dir,'rock')
os.mkdir(train_rock_dir)
train_stop_dir = os.path.join(train_dir,'stop')
os.mkdir(train_stop_dir)
train_stop_invert_dir = os.path.join(train_dir,'stop_invert')
os.mkdir(train_stop_invert_dir)
train_three_dir = os.path.join(train_dir,'three')
os.mkdir(train_three_dir)
train_three2_dir = os.path.join(train_dir,'three2')
os.mkdir(train_three2_dir)
train_two_up_dir = os.path.join(train_dir,'two_up')
os.mkdir(train_two_up_dir)
train_two_up_invert_dir = os.path.join(train_dir,'two_up_invert')
os.mkdir(train_two_up_invert_dir)

test_call_dir = os.path.join(test_dir,'call')
os.mkdir(test_call_dir)
test_dislike_dir = os.path.join(test_dir,'dislike')
os.mkdir(test_dislike_dir)
test_fist_dir = os.path.join(test_dir,'fist')
os.mkdir(test_fist_dir)
test_four_dir = os.path.join(test_dir,'four')
os.mkdir(test_four_dir)
test_like_dir = os.path.join(test_dir,'like')
os.mkdir(test_like_dir)
test_mute_dir = os.path.join(test_dir,'mute')
os.mkdir(test_mute_dir)
test_ok_dir = os.path.join(test_dir,'ok')
os.mkdir(test_ok_dir)
test_one_dir = os.path.join(test_dir,'one')
os.mkdir(test_one_dir)
test_palm_dir = os.path.join(test_dir,'palm')
os.mkdir(test_palm_dir)
test_peace_dir = os.path.join(test_dir,'peace')
os.mkdir(test_peace_dir)
test_peace_invert_dir = os.path.join(test_dir,'peace_invert')
os.mkdir(test_peace_invert_dir)
test_rock_dir = os.path.join(test_dir,'rock')
os.mkdir(test_rock_dir)
test_stop_dir = os.path.join(test_dir,'stop')
os.mkdir(test_stop_dir)
test_stop_invert_dir = os.path.join(test_dir,'stop_invert')
os.mkdir(test_stop_invert_dir)
test_three_dir = os.path.join(test_dir,'three')
os.mkdir(test_three_dir)
test_three2_dir = os.path.join(test_dir,'three2')
os.mkdir(test_three2_dir)
test_two_up_dir = os.path.join(test_dir,'two_up')
os.mkdir(test_two_up_dir)
test_two_up_invert_dir = os.path.join(test_dir,'two_up_invert')
os.mkdir(test_two_up_invert_dir)

valid_call_dir = os.path.join(valid_dir,'call')
os.mkdir(valid_call_dir)
valid_dislike_dir = os.path.join(valid_dir,'dislike')
os.mkdir(valid_dislike_dir)
valid_fist_dir = os.path.join(valid_dir,'fist')
os.mkdir(valid_fist_dir)
valid_four_dir = os.path.join(valid_dir,'four')
os.mkdir(valid_four_dir)
valid_like_dir = os.path.join(valid_dir,'like')
os.mkdir(valid_like_dir)
valid_mute_dir = os.path.join(valid_dir,'mute')
os.mkdir(valid_mute_dir)
valid_ok_dir = os.path.join(valid_dir,'ok')
os.mkdir(valid_ok_dir)
valid_one_dir = os.path.join(valid_dir,'one')
os.mkdir(valid_one_dir)
valid_palm_dir = os.path.join(valid_dir,'palm')
os.mkdir(valid_palm_dir)
valid_peace_dir = os.path.join(valid_dir,'peace')
os.mkdir(valid_peace_dir)
valid_peace_invert_dir = os.path.join(valid_dir,'peace_invert')
os.mkdir(valid_peace_invert_dir)
valid_rock_dir = os.path.join(valid_dir,'rock')
os.mkdir(valid_rock_dir)
valid_stop_dir = os.path.join(valid_dir,'stop')
os.mkdir(valid_stop_dir)
valid_stop_invert_dir = os.path.join(valid_dir,'stop_invert')
os.mkdir(valid_stop_invert_dir)
valid_three_dir = os.path.join(valid_dir,'three')
os.mkdir(valid_three_dir)
valid_three2_dir = os.path.join(valid_dir,'three2')
os.mkdir(valid_three2_dir)
valid_two_up_dir = os.path.join(valid_dir,'two_up')
os.mkdir(valid_two_up_dir)
valid_two_up_invert_dir = os.path.join(valid_dir,'two_up_invert')
os.mkdir(valid_two_up_invert_dir)

count_test = 100
count_train = 1000
count_valid = 100

fnames = os.listdir(original_dataset_dir_call)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_call, fname)
    dst = os.path.join(train_call_dir,fname)
    print(dst)
    shutil.copyfile(src, dst)

fnames = os.listdir(original_dataset_dir_call)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_call, fname)
    dst = os.path.join(test_call_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_call)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_call,fname)
    dst = os.path.join(valid_call_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end call")

fnames = os.listdir(original_dataset_dir_dislike)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_dislike, fname)
    dst = os.path.join(train_dislike_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_dislike)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_dislike, fname)
    dst = os.path.join(test_dislike_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_dislike)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_dislike,fname)
    dst = os.path.join(valid_dislike_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end dislike")
fnames = os.listdir(original_dataset_dir_fist)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_fist, fname)
    dst = os.path.join(train_fist_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_fist)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_fist, fname)
    dst = os.path.join(test_fist_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_fist)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_fist,fname)
    dst = os.path.join(valid_fist_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end fist")
fnames =  os.listdir(original_dataset_dir_four)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_four, fname)
    dst = os.path.join(train_four_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_four)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_four, fname)
    dst = os.path.join(test_four_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_four)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_four,fname)
    dst = os.path.join(valid_four_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end four")
fnames =  os.listdir(original_dataset_dir_like)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_like, fname)
    dst = os.path.join(train_like_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_like)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_like, fname)
    dst = os.path.join(test_like_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_like)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_like,fname)
    dst = os.path.join(valid_four_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end like")
fnames = os.listdir(original_dataset_dir_mute)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_mute, fname)
    dst = os.path.join(train_mute_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_mute)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_mute, fname)
    dst = os.path.join(test_mute_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_mute)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_mute,fname)
    dst = os.path.join(valid_mute_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end mute")
fnames = os.listdir(original_dataset_dir_ok)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_ok, fname)
    dst = os.path.join(train_ok_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_ok)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_ok, fname)
    dst = os.path.join(test_ok_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_ok)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_ok,fname)
    dst = os.path.join(valid_mute_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end ok")
fnames = os.listdir(original_dataset_dir_one)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_one, fname)
    dst = os.path.join(train_one_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_one)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_one, fname)
    dst = os.path.join(test_one_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_one)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_one,fname)
    dst = os.path.join(valid_one_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end one")
fnames = os.listdir(original_dataset_dir_palm)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_palm, fname)
    dst = os.path.join(train_palm_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_palm)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_palm, fname)
    dst = os.path.join(test_palm_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_palm)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_palm,fname)
    dst = os.path.join(valid_palm_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end palm")
fnames = os.listdir(original_dataset_dir_peace)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_peace, fname)
    dst = os.path.join(train_peace_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_peace)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_peace, fname)
    dst = os.path.join(test_peace_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_peace)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_peace,fname)
    dst = os.path.join(valid_peace_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end peace")
fnames = os.listdir(original_dataset_dir_peace_invert)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_peace_invert, fname)
    dst = os.path.join(train_peace_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_peace_invert)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_peace_invert, fname)
    dst = os.path.join(test_peace_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_peace_invert)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_peace_invert,fname)
    dst = os.path.join(valid_peace_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end peace_invert")
fnames = os.listdir(original_dataset_dir_rock)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_rock, fname)
    dst = os.path.join(train_rock_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_rock)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_rock, fname)
    dst = os.path.join(test_rock_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_rock)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_rock,fname)
    dst = os.path.join(valid_rock_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end rock")
fnames = os.listdir(original_dataset_dir_stop)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_stop, fname)
    dst = os.path.join(train_stop_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_stop)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_stop, fname)
    dst = os.path.join(test_stop_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_stop)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_stop,fname)
    dst = os.path.join(valid_stop_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end stop")
fnames = os.listdir(original_dataset_dir_stop_invert)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_stop_invert, fname)
    dst = os.path.join(train_stop_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_stop_invert)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_stop_invert, fname)
    dst = os.path.join(test_stop_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_stop_invert)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_stop_invert,fname)
    dst = os.path.join(valid_stop_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end stop invert")
fnames = os.listdir(original_dataset_dir_three)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_three, fname)
    dst = os.path.join(train_three_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_three)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_three, fname)
    dst = os.path.join(test_three_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_three)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_three,fname)
    dst = os.path.join(valid_three_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end three")
fnames = os.listdir(original_dataset_dir_three2)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_three2, fname)
    dst = os.path.join(train_three2_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_three2)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_three2, fname)
    dst = os.path.join(test_three2_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_three2)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_three2,fname)
    dst = os.path.join(valid_three2_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end three2")
fnames = os.listdir(original_dataset_dir_two_up)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_two_up, fname)
    dst = os.path.join(train_two_up_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_two_up)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_two_up, fname)
    dst = os.path.join(test_two_up_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_two_up)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_two_up,fname)
    dst = os.path.join(valid_two_up_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end two_up")
fnames = os.listdir(original_dataset_dir_two_up_invert)[:count_train]
for fname in fnames:
    src = os.path.join(original_dataset_dir_two_up_invert, fname)
    dst = os.path.join(train_two_up_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_two_up_invert)[count_train:count_train+count_test]
for fname in fnames:
    src = os.path.join(original_dataset_dir_two_up_invert, fname)
    dst = os.path.join(test_two_up_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)

fnames = os.listdir(original_dataset_dir_two_up_invert)[count_train+count_test:count_train+count_test+count_valid]
for fname in fnames:
    src = os.path.join(original_dataset_dir_two_up_invert,fname)
    dst = os.path.join(valid_two_up_invert_dir,fname)
    print(dst)
    shutil.copyfile(src,dst)
print("end two_up_invert")