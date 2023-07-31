# -*- coding: utf-8 -*-
import json



class BackResult:
    
    
    def __init__(self, success, code, message, content):
        self.success = success
        self.code = code
        self.message = message
        self.content = content
    
       
    @staticmethod
    def SUCCESS(content=[]):
        return BackResult(True, 200, "success", content)
        

if __name__ == '__main__':
    
    back=BackResult(True, 206, "验证json转换", [])
    jsonstr = json.dumps(back.__dict__)
    print(back.code)
    print(jsonstr)
    back.code=779
    print(json.dumps(back.__dict__))
    #
  
    print(json.dumps(BackResult.SUCCESS().__dict__))