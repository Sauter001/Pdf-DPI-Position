from pdf2image import convert_from_path
import cv2
import os

height, width = 0, 0


def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(
            f"Position: {int(round(x * 72 / 100, 0))}, {int(round((height / 2 - y) * 72 / 100 - 5, 0))}"
        )


def get_cursor_coordinates():
    # 페이지 번호 입력
    page_number = int(input("페이지 번호: "))

    # 사용할 PDF
    pdf_file_path = "file.pdf"

    pages = convert_from_path("./" + pdf_file_path)

    # pdf 이미지 변환 후 /source에 넣음
    for i, page in enumerate(pages):
        if not os.path.isfile("./source/" + "file" + "_" + str(i) + ".png"):
            page.save("./source/" + "file" + "_" + str(i) + ".png", "PNG")

    global height, width
    img = cv2.imread("./source/" + "file" + "_" + str(page_number - 1) + ".png")
    height, width = img.shape[:2]
    img = cv2.resize(img, dsize=(width // 2, height // 2))
    cv2.namedWindow("Page Image")
    # cv2.namedWindow("Page Image", cv2.WINDOW_NORMAL) # 하단 좌표 확인할 시 활성화. 사진이 세로로 압축됨

    cv2.imshow("Page Image", img)
    cv2.setMouseCallback("Page Image", on_mouse_click)

    # 윈도우 닫기 대기
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    get_cursor_coordinates()
