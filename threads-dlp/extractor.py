import requests

def extractor(url: str) -> str:
    headers = {
        ":authority": "scontent.cdninstagram.com",
        ":method": "GET",
        ":path": "/o1/v/t2/f2/m86/AQNFy2WyVfqe3Q6VPnKrR4ya8S5jV7ZDqtx7EQwt5Xv1OfCTaFU5hdO0ik3WNd-6Qzao5h4hTAcEooxUq2q8AaO5AdWrL8uNT0rfI_Y.mp4?_nc_cat=101&_nc_oc=AdkE_QKELd7VSrZPWC21NElELltD6Rqys9CigCKxROkIIt9rKGwePnxBQVqbYSOYzVWSSHOeDHd29xXwQovVS28y&_nc_sid=5e9851&_nc_ht=instagram.foua4-1.fna.fbcdn.net&_nc_ohc=T4qj90FGTdkQ7kNvwFzG_15&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uRkVFRC5DMy43MjAuZGFzaF9iYXNlbGluZV8xX3YxIiwieHB2X2Fzc2V0X2lkIjoxMDc1MzYwNjg0NTA2MzY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=8b76ed49394fec45&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8zNDREMkFCQzhGOEJFNkRENjI5QTFEQUMxMzM5MTA4OF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTjlTbFI1NEtycE8xNEVDQUh2RzdvZ2l5YTlPYnFfRUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm_PPXuZ2C6QMVAigCQzMsF0AZmZmZmZmaGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXqB2XmnQEA&_nc_zt=28&oh=00_AfODbVAbu0r76BDCCCkMgh_x5Zt-YEdnUGvwDNLaP5aRvA&oe=685E16AA",
        ":scheme": "https",
        "accept": "*/*",
        "accept-encoding": "identity;q=1, *;q=0",
        "accept-language": "en-US,en;q=0.9",
        "priority": "i",
        "range": "bytes=0-",
        "referer": "https://scontent.cdninstagram.com/o1/v/t2/f2/m86/AQNFy2WyVfqe3Q6VPnKrR4ya8S5jV7ZDqtx7EQwt5Xv1OfCTaFU5hdO0ik3WNd-6Qzao5h4hTAcEooxUq2q8AaO5AdWrL8uNT0rfI_Y.mp4?_nc_cat=101&_nc_oc=AdkE_QKELd7VSrZPWC21NElELltD6Rqys9CigCKxROkIIt9rKGwePnxBQVqbYSOYzVWSSHOeDHd29xXwQovVS28y&_nc_sid=5e9851&_nc_ht=instagram.foua4-1.fna.fbcdn.net&_nc_ohc=T4qj90FGTdkQ7kNvwFzG_15&efg=eyJ2ZW5jb2RlX3RhZyI6Inhwdl9wcm9ncmVzc2l2ZS5JTlNUQUdSQU0uRkVFRC5DMy43MjAuZGFzaF9iYXNlbGluZV8xX3YxIiwieHB2X2Fzc2V0X2lkIjoxMDc1MzYwNjg0NTA2MzY2LCJ2aV91c2VjYXNlX2lkIjoxMDA5OSwiZHVyYXRpb25fcyI6NiwidXJsZ2VuX3NvdXJjZSI6Ind3dyJ9&ccb=17-1&vs=8b76ed49394fec45&_nc_vs=HBksFQIYUmlnX3hwdl9yZWVsc19wZXJtYW5lbnRfc3JfcHJvZC8zNDREMkFCQzhGOEJFNkRENjI5QTFEQUMxMzM5MTA4OF92aWRlb19kYXNoaW5pdC5tcDQVAALIARIAFQIYOnBhc3N0aHJvdWdoX2V2ZXJzdG9yZS9HTjlTbFI1NEtycE8xNEVDQUh2RzdvZ2l5YTlPYnFfRUFBQUYVAgLIARIAKAAYABsCiAd1c2Vfb2lsATEScHJvZ3Jlc3NpdmVfcmVjaXBlATEVAAAm_PPXuZ2C6QMVAigCQzMsF0AZmZmZmZmaGBJkYXNoX2Jhc2VsaW5lXzFfdjERAHXqB2XmnQEA&_nc_zt=28&oh=00_AfODbVAbu0r76BDCCCkMgh_x5Zt-YEdnUGvwDNLaP5aRvA&oe=685E16AA",
        "sec-ch-ua": "'Google Chrome';v='137', 'Chromium';v='137', 'Not/A)Brand';v='24",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "video",
        "sec-fetch-mode": "no-cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    }
