from downloader import downloader
from extractor import extractor
import argparse

def main():
    import sys
    
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} URL")
        exit(0)
        
    url = sys.argv[1]
    
    ret, video_url = extractor(url)
    if ret: 
        downloader(url, video_url)
    else:
        print(video_url)
    
if __name__ == '__main__':
    main()