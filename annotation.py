import requests

url = "https://api.formant.io/v1/admin/annotations"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer eyJraWQiOiJmUkNjSDdYM0xRVnZBaE5HQ1lqR3RNaFppQ0NucG5hdHBEbTN0TWFBR0xBPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0NWM4MDI3NC00YjIwLTQ5ZDktYjIxNi04NzNmODhhMDk5Y2IiLCJjb2duaXRvOmdyb3VwcyI6WyJzdXBlcnVzZXIiXSwiZW1haWxfdmVyaWZpZWQiOnRydWUsImN1c3RvbTpvcmdhbml6YXRpb25faWQiOiJkMGM3OTc3OS1jNjNmLTRiN2UtOTBkNC1lMGEyMDI1OTk4YjciLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtd2VzdC0yLmFtYXpvbmF3cy5jb21cL3VzLXdlc3QtMl9PU0JuRHhCY3oiLCJjb2duaXRvOnVzZXJuYW1lIjoiNDVjODAyNzQtNGIyMC00OWQ5LWIyMTYtODczZjg4YTA5OWNiIiwiYXVkIjoiM3BncGEyOGlvaWxrcGdpOGFoZzl2NmdjbGoiLCJldmVudF9pZCI6IjU3MGY2MGNmLTY3YTgtNDAzMi1hNzY5LWY5OTRmMjdiZmZhOCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNjgzMTQxNzE4LCJleHAiOjE2ODMxNTc4MDMsImlhdCI6MTY4MzE1NDIwMywiZW1haWwiOiJxYSsxK3ZlcmlmaWVkQGZvcm1hbnQuaW8ifQ.JTES-yEqfoRR0JnDQ--X3nc65XTLRLd8K1pS1uuf-5KlRypsQUX093pwS93t3oQb5IVT8cUogrXu1FHdrXs6ukkMJg_NWf61mlZv-eH4_d47uBtZy21UMEkOftlbdjR-Wni3YaZjiBs4OPN6mGo2dGoD1EQcYMF3F93wKolIytepwc7tbATsJ-PKyy0rE9Avp2b0heK5S5yT0Htb7z21K6d6mdR20IsCqQyiuSWdMdHVGX4HPb55MHcUp6LZfNG0tz_popbljYE2r9mroWUsvTnZD8ivPd4AefpOudnso2_i905F3vr5pEoS8PRCvjHHWGTHZuFIgt73V4WtDspjyg"
}

response = requests.post(url, headers=headers)

print(response.text)