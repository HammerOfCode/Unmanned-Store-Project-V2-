import READQRCODE2
import cv2 
import facial_req
import client 




cap = cv2.VideoCapture(0)
def main():
    while True:
        
        ret, frame = cap.read()
        READQRCODE2.decoder(frame)
        cv2.imshow('Image', frame)
        code = cv2.waitKey(50)
        
        if code == ord('q'):
            break
        elif code == ord('l'):
            print(READQRCODE2.qrlist)
        elif code == ord('s'):
            
            client.send(str(READQRCODE2.qrlist))   
        elif code == ord('d'):
            client.send(client.DISCONNECT_MESSAGE)
            

main()
if __name__ == "__main__":
     main()