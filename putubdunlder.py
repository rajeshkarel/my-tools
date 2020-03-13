import youtube_dl #module required to download youtube videos
y= {} 
# while (1): 
# link= input("Copy & paste the URL of the YouTube video you want to download:- ") 
link="https://www.youtube.com/watch?v=mDoHtD1hI3I&list=PLC3y8-rFHvwhBRAgFinJR8KHIrCdTkZcZ&index=3"
youtube_dl.YoutubeDL(y).download([link])
# f=input("\nENETR YES(Y) TO CONTINUE DOWNLOADING VIDEOS \nELSE NO(N) TO STOP\n") 
# if f=="N" or f=="n":
#     break