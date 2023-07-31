# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 18:09:31 2023

@author: yang
"""

import os
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
# import sys


class OssDef:
    def __init__(self, Manual=None):
        self.secret_id = 'AKIDJI8mCOM7fy42oNiroXw75rPjohNp34sd'
        self.secret_key = 'a7YoqeFclhRxFJ9l392lKjvxnTzJRPDo'
        self.region = 'ap-nanjing'
        self.token = None
        self.scheme = 'https'
        self.bckt_id = 'stable-1305002912'
        # sys.setrecursionlimit(10000)
        config = CosConfig(Region=self.region, SecretId=self.secret_id, SecretKey=self.secret_key, Token=self.token, Scheme=self.scheme)
        self.bucket = CosS3Client(config, retry=3)

    # 判断文件存在
    def is_exist(self, oss_path):
        exist = self.bucket.object_exists(self.bckt_id, oss_path)
        return exist

    # 获取可访问的url
    def get_object_compressed(self, oss_path, expirate=60):
        result = self.bucket.get_object_url(self.bckt_id, oss_path)
        return result

    # 文件上传
    def upload(self, obj_data, oss_path):
        """
        :param obj_data: 二进制数据
        :param oss_path: 上传到oss的路径
        :return:
        """
        result = self.bucket.put_object(Bucket=self.bckt_id, Body=obj_data, Key=oss_path)
        check_res = self.is_exist(oss_path)
        return result['ETag'] if check_res else check_res

    # 下载文件
    def download(self, oss_path, dest_path=None):
        result = False
        if self.is_exist(oss_path):  # 若cos上存在该文件，则
            result = self.bucket.download_file(Bucket=self.bckt_id, Key=oss_path, DestFilePath=dest_path)  # 下载
            if os.path.isfile(dest_path):  # 若下完，在本地有这个文件，则
                result = True
        return result

    # 删除图片
    def del_img(self, oss_path):
        self.bucket.delete_object(self.bckt_id, oss_path)  # 删除，并返回结果
        if not self.is_exist(oss_path):  # 若cos上文件不在了
            return True
        return False

    # 访问文件列表
    def require_list(self, prefix):
        res = self.bucket.list_objects(Bucket=self.bckt_id, Prefix=prefix)
        if res.get('Contents') and res['Contents']:
            return [i['Key'] for i in res['Contents']]
        return []

    # 获取文件大小
    def require_size(self, oss_path):
        size = 0
        if self.is_exist(oss_path=oss_path):
            size = self.bucket.head_object(Bucket=self.bckt_id, Key=oss_path)['Content-Length']
        return size


if __name__ == '__main__':
    
    '''访问文件列表'''
    ossdef = OssDef()
    key_of_file="/sam/lxiaodao/2023-7-26/union777abc9999.jpg"
    with open('D:/成都尚恩未来科技/AI/shirt-another.jpg', 'rb') as fp:
         returns=ossdef.upload(fp, key_of_file)
         print(1,returns)
    #file_list = bucket.require_list(prefix='test04-123456789-image')
    #print(2, file_list)
    
    #is_cuccess=bucket.download(key_of_file, "D:/download/aa.jpg")
    #print(is_cuccess)
    url =ossdef.get_object_compressed(key_of_file)
    print(url)

    # print(bucket.is_exist(oss_path='cache/master/asm/parts/111894'))
    # file_list = bucket.require_list(prefix='cache/master/asm/parts/111894')
    # print(1, file_list)
    # print(list(filter(lambda x: '.glb' in x, bucket.require_list(prefix=f"cache/master/asm/parts/414076"))))
    # '''下载文件'''
    # bucket.download('cache/local/asm/parts/3333/3067/0.glb', dest_path='wrnmmmp.glb')
    # '''上传文件'''
    # with open('wrnmmmp.glb', 'rb') as f:
    #     bucket.upload(obj_data=f, oss_path='1350/1027/wrnmmmp.glb')
    # file_list = bucket.require_list(prefix='1350/')
    # print(2, file_list)
    # '''删除文件'''
    # bucket.del_img(oss_path='1350/1027/wrnmmmp.glb')
    # file_list = bucket.require_list(prefix='1350/')
    # print(3, file_list)
    # slice_list = bucket.require_list('cache/local/asm/parts/10088/')
    # slice_dir_list = {i.split('/')[-2]: list(filter(lambda x: i.split('/')[-2] in x and '.glb' in x, slice_list)) for i in slice_list if '.glb' in i}
    # print(slice_dir_list)



