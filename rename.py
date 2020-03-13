import os

os.chdir(r'C:\Users\rajes\OneDrive\Desktop\harry latest')

for f in os.listdir():
    print(f)
    file_name, file_ext = os.path.splitext(f)
    f_title, f_num_str = file_name.split('#')
    temp = f_title.split("_")
    v_title, t_title = temp[0], temp[1]
    t_num1 = f_num_str.split("-")
    t_num = t_num1[0]
    new_name = '{}-{}{}'.format(t_num.strip().zfill(3), v_title.strip(), file_ext.strip())
    print("renamed as per below: ")
    print(new_name)
    os.rename(f, new_name)
    print("Done.")


# print(len(os.listdir()))