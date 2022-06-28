import requests

def  get_data():
  headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
  }

  for i in range(1, 49):
    url = f'https://www.recordpower.co.uk/flip/Winter2020/files/mobile/{i}.jpg'
    req = requests.get(url=url, headers=headers)
    response = req.content

    with open(f'media/{i}.jpg', 'wb') as file:
      file.write(response)
      print(f'Download {i} of 48')

def main():
  get_data()

if __name__ == '__main__':
  main()