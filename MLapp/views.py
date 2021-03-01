from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage


  # text recognition
import cv2
import os 
from PIL import Image 
import pytesseract as pt
from pytesseract import image_to_string 


def home_view(request):
  return render(request, "pages/home.html",context={})


def select_pic_view(request):
  if request.method == 'POST':
        if 'myfile' not in request.FILES:
            return HttpResponseNotFound('<center><h1>File not uploaded ,<br> Upload the file for getting the desired result....</h1></center>')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
    
        path ="media"
        for imageName in os.listdir(path):
              inputPath = os.path.join(path, imageName) 
              img = Image.open(inputPath) 
  
             # applying ocr using pytesseract for python 
              text = pt.image_to_string(img, lang ="eng") 
        
              fullTempPath = os.path.join('extracted'".txt") 
              print(text)
              text = text.split('\n')
              # print(text)
        file1 = open(fullTempPath, "a+") 
        # providing the content in the image 
        file1.write(' '.join(map(str, text)))
        file1.close()  
         # for printing the output file 
        file2 = open(fullTempPath, 'r') 
        print(file2.read()) 
        file2.close()
        f = open('extracted.txt', 'r')
        file_content = f.read()
        f.close()  
        context = {
            'uploaded_file_url': uploaded_file_url ,
            'text':text,
            'file_content' : file_content
        }
        return render(request, "pages/select_images.html", context)
       
      
  return render(request,"pages/select_images.html")

def camera(request):
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("")

    img_counter = 0
    while True:
          ret, frame = cam.read()
          if not ret:
              print("failed to grab frame")
              break
          cv2.imshow("test", frame)

          k = cv2.waitKey(1)
          if k%256 == 27:
              # ESC pressed
              print("Escape hit, closing...")
              break
          elif k%256 == 32:
              # SPACE pressed
              img_name = "capture_image/opencv_frame_{}.png".format(img_counter)
              cv2.imwrite(img_name, frame)
              print("{} written!".format(img_name))
              img_counter += 1

              path ="capture_image"
              for imageName in os.listdir(path):
                      inputPath = os.path.join(path, imageName) 
                      img = Image.open(inputPath) 
          
                      # applying ocr using pytesseract for python 
                      text = pt.image_to_string(img, lang ="eng") 
                  
                      fullTempPath = os.path.join('capture_extracted'".txt") 
                      print(text)
                      text = text.split('\n')
                    
    cam.release()

    cv2.destroyAllWindows()
    return render(request,"pages/capture.html" ,{'text':text})




