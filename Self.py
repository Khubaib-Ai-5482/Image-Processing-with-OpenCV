import cv2
import numpy as np

path = input("Enter the path of image:")
x_size = int(input("x_size:"))
y_size = int(input("Y_size:"))
size = (x_size,y_size)

image = cv2.imread(path)
image = cv2.resize(image,size)

while True:
    print("""
    1. put text
    2. image stacking
    3. Draw shapes
    4. Blend two images
    5. EDGE DETECTION
    6. ADD BORDER
    7. Blurring
    8. Convert To GrayScale
    """)

    choice = int(input("Enter your choice:"))

    if choice == 1:
        text = input("enter your text:")
        x = int(input("enter x position:"))
        y = int(input("Enter y position:"))
        position = (x,y)
        font = cv2.FONT_HERSHEY_COMPLEX
        font_scale = int(input("Scale size:"))
        B = int(input("Enter Blue value(0-255):"))
        G = int(input("Enter Green value(0-255):"))
        R = int(input("Enter Red value(0-255):"))
        color = (B,G,R)
        thickness= int(input("Enter thickness:"))
        cv2.putText(image,text,position,font,font_scale,color,thickness)
        cv2.imshow("Myimg",image)

    elif choice == 2:
        stack = input("Number of images you want to stack(limit = three) and select format(h/v):").lower().split()
        if len(stack) == 2:
            num,mode = stack[0],stack[1]

            if num == "one" and mode == "v":
                stacked_img = np.vstack((image,image))
                cv2.imshow("Img",stacked_img)

            elif num == "one" and mode == "h":
                stacked_img = np.hstack((image,image))
                cv2.imshow("Img",stacked_img)

            elif num == "two" and mode == "v":
                sec_img_path = input("Enter path of 2nd img:")
                sec_img = cv2.imread(sec_img_path)
                sec_img = cv2.resize(sec_img,size)
                stacked_img = np.vstack((image,sec_img))
                cv2.imshow("Img",stacked_img)

            elif num == "two" and mode == "h":
                sec_img_path = input("Enter path of 2nd img:")
                sec_img = cv2.imread(sec_img_path)
                sec_img = cv2.resize(sec_img,size)
                stacked_img = np.hstack((image,sec_img))
                cv2.imshow("Img",stacked_img)

            elif num == "three" and mode == "v":
                sec_img_path = input("Enter path of 2nd img:")
                sec_img = cv2.imread(sec_img_path)
                sec_img = cv2.resize(sec_img,size)              
                third_img_path = input("Enter path of 3rd img:")
                third_img = cv2.imread(third_img_path)  
                third_img = cv2.resize(third_img,size)
                stacked_img = np.vstack((image,sec_img,third_img))
                cv2.imshow("Img",stacked_img) 

            elif num == "three" and mode == "h":
                sec_img_path = input("Enter path of 2nd img:")
                sec_img = cv2.imread(sec_img_path)
                sec_img = cv2.resize(sec_img,size)              
                third_img_path = input("Enter path of 3rd img:")
                third_img = cv2.imread(third_img_path)  
                third_img = cv2.resize(third_img,size)
                stacked_img = np.hstack((image,sec_img,third_img))
                cv2.imshow("Img",stacked_img)          
            else:
                print("Error")
                break

    elif choice == 3:
        print("""
            1-rectangle
            2-circle
            3-ellipse""")
    
        sel_shape = int(input("Select your shape:"))
        if sel_shape == 1:
            x1 = int(input("Enter top-left X: "))
            y1 = int(input("Enter top-left Y: "))
            top_left = (x1, y1)
            x2 = int(input("Enter bottom-right X: "))
            y2 = int(input("Enter bottom-right Y: "))
            bottom_right = (x2, y2)
            B = int(input("Enter Blue value(0-255):"))
            G = int(input("Enter Green value(0-255):"))
            R = int(input("Enter Red value(0-255):"))
            color = (B,G,R)
            thickness= int(input("Enter thickness:"))
            cv2.rectangle(image,top_left,bottom_right,color,thickness)
            cv2.imshow("img",image)

        elif sel_shape == 2:
            x=int(input("Enter x:"))
            y=int(input("enter y:"))
            x_y = (x,y)
            radius = int(input("Enter radius:"))
            B = int(input("Enter Blue value(0-255):"))
            G = int(input("Enter Green value(0-255):"))
            R = int(input("Enter Red value(0-255):"))
            color = (B,G,R)
            thickness_cir = int(input("Enter thickness:"))
            cv2.circle(image,x_y,radius,color,thickness_cir)
            cv2.imshow("myimg",image)

        elif sel_shape == 3:
            x = int(input("Enter x:"))
            y = int(input("Enter y:"))
            center= (x,y)
            major_axis = int(input("Major axis:"))
            minor_axis = int(input("Minor axis:"))
            axis_len = (major_axis,minor_axis)
            rotation = int(input("Rotation:"))
            starting_angle = int(input("Starting angle:"))
            ending_angle = int(input("Ending angle:"))
            B = int(input("Enter Blue value(0-255):"))
            G = int(input("Enter Green value(0-255):"))
            R = int(input("Enter Red value(0-255):"))
            color = (B,G,R)
            thickness_cir = int(input("Enter thickness:"))
            cv2.ellipse(image,center,axis_len,rotation,starting_angle,ending_angle,color,thickness_cir)
            cv2.imshow("myimg",image)

    elif choice == 4:

        sec_img_path = input("Enter path of 2nd image: ")
        sec_img = cv2.imread(sec_img_path)   
        sec_img = cv2.resize(sec_img, size)
        blended = cv2.addWeighted(image,0.5,sec_img,0.5,1)
        cv2.imshow("My image",blended)
    
    elif choice == 5:

        threshold1 = int(input("Enter threshod_1:"))
        threshold2 = int(input("Enter threshod_2:"))
        apertureSize= int(input("apertureSize(3/5/7):"))
        edges = cv2.Canny(image,threshold1,threshold2,apertureSize,L2gradient=True)
        cv2.imshow("Img",edges)
    
    elif choice == 6:
        Top = int(input("Enter top value:"))
        Bottom = int(input("Enter bottom value:"))
        Left = int(input("Enter left value:"))
        Right = int(input("Enter right value:"))
        bordered = cv2.copyMakeBorder(image,Top,Bottom,Left,Right,cv2.BORDER_ISOLATED)
        cv2.imshow("IMG",bordered)
    
    elif choice == 7:
        print("1-Guassion Blur,2-Median Blur,3-Bilateral Filter")
        select_function = int(input("Select your function:"))

        if select_function == 1:
            G=  cv2.GaussianBlur(image, (7, 7), 0)
            cv2.imshow("My IMG",G)

        elif select_function == 2:
            m = cv2.medianBlur(image, 5)
            cv2.imshow("My IMG",m)

        elif select_function == 3:
            b = cv2.bilateralFilter(image, 10, 100, 100)
            cv2.imshow("My IMG",b)
    

    elif choice == 8:

        new = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Grayscale Image", new)

    

    else:
        print("Error")

    cv2.waitKey(0)
    cv2.destroyAllWindows()







