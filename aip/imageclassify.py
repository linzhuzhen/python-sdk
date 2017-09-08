
# -*- coding: utf-8 -*-

"""
图像识别
"""

import re
import sys
import math
import time
from .base import AipBase
from .base import base64
from .base import json
from .base import urlencode
from .base import quote
from .base import StringIO

class AipImageClassify(AipBase):
    """
    图像识别
    """

    __dishDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/dish'

    __carDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/car'

    __logoSearchUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/logo'

    __logoAddUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/v1/logo/add'

    __logoDeleteUrl = 'https://aip.baidubce.com/rest/2.0/realtime_search/v1/logo/delete'

    __objectDetectUrl = 'https://aip.baidubce.com/rest/2.0/image-classify/v1/object_detect'

    
    def dishDetect(self, image, options=None):
        """
            菜品识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__dishDetectUrl, data)
    
    def carDetect(self, image, options=None):
        """
            车辆识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__carDetectUrl, data)
    
    def logoSearch(self, image, options=None):
        """
            logo商标识别
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__logoSearchUrl, data)
    
    def logoAdd(self, image, brief, options=None):
        """
            logo入库
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)
        data['brief'] = brief

        data = dict(data, **options)

        return self._request(self.__logoAddUrl, data)
    
    def logoDeleteByImage(self, image, options=None):
        """
            删除logo
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__logoDeleteUrl, data)
    
    def logoDeleteBySign(self, cont_sign, options=None):
        """
            删除logo
        """
        options = options or {}

        data = {}
        data['cont_sign'] = cont_sign

        data = dict(data, **options)

        return self._request(self.__logoDeleteUrl, data)
    
    def objectDetect(self, image, options=None):
        """
            图像主体检测
        """
        options = options or {}

        data = {}
        data['image'] = base64.b64encode(image)

        data = dict(data, **options)

        return self._request(self.__objectDetectUrl, data)
    