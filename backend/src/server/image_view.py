# import json
# import numpy as np
# from flask_restful import Resource, reqparse
# from flask import abort, request
# from common.server.flaskutils import flask_log
# import cv2
# from image_processing.strike_checker import StrikeChecker

# # parser = reqparse.RequestParser()
# # parser.add_argument('im', type=str)
# # parser.add_argument('res')

# image_width = 0
# image_height = 0
# striker = StrikeChecker()

# def rgba2rgb(rgba_array, w, h):
#     rgb_array = np.zeros((w, h, 3))
#     for j in range(h):
#         for i in range(w):
#             rgb_array[i,j,0] = rgba_array[4*(w*j+ i)]
#             rgb_array[i,j,1] = rgba_array[4*(w*j+ i) + 1]
#             rgb_array[i,j,2] = rgba_array[4*(w*j+ i) + 2]
#     return rgb_array

# def rgba2bgr(rgba_array, w, h):
#     rgb_array = np.zeros((w, h, 3))
#     for j in range(h):
#         for i in range(w):
#             rgb_array[i,j,0] = rgba_array[4*(w*j+ i) + 2]
#             rgb_array[i,j,1] = rgba_array[4*(w*j+ i) + 1]
#             rgb_array[i,j,2] = rgba_array[4*(w*j+ i)]
#     return rgb_array

# class ImageView(Resource):
#     def post(self):
#         global striker
#         image = np.fromstring(request.data[126:126 + 4*image_width*image_height], dtype=np.uint8)
#         if striker.check(rgba2bgr(image, image_width, image_height)):
#             return {'strike': 'Out'}
#         else:
#             return {'strike': 'In'}

# class ImageSettings(Resource):
#     def post(self):
#         global image_width
#         global image_height
#         settings_parser = reqparse.RequestParser()
#         settings_parser.add_argument('width', type=int)
#         settings_parser.add_argument('height', type=int)
#         args = settings_parser.parse_args()

#         image_width = args.get('width', 0)
#         image_height = args.get('height', 0)

#         if image_height > 0 and image_width > 0:
#             return {'valid': True}
#         else:
#             return {'valid': False}
