import cv2
import bottle


@bottle.route('/hello')
def hello():
    return "Hello World!"


def convert_image_to_video():
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    video = cv2.VideoWriter('video.mp4', fourcc, 20.0, (640, 480))

    for i in range(1, 5):
        img = cv2.imread('image{0:03d}.png'.format(i))
        img = cv2.resize(img, (640, 480))
        video.write(img)

    video.release()


if __name__ == "__main__":
    bottle.run(host='localhost', port=8080, debug=True)
