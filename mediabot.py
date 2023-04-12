from aiogram import Bot,Dispatcher,executor,types
import requests
API="5998727959:AAEtKxyH923xaWHPjySIvSEIs_5Gp9KhnGw"
bot=Bot(token=API)
dp=Dispatcher(bot)
@dp.message_handler(commands=['start'])
async def salomlash(xabar: types.Message):
    # print(xabar.from_user.id)
    await xabar.reply(f"Assalomu alaykum, {xabar.from_user.mention}")

@dp.message_handler(commands=['help'])
async def yordam(xabar: types.Message):
    await xabar.answer("/start - buyrug'ini bosish orqali botni qayta ishga tushurish mumkin !"
@dp.message_handler()
async def echo(xabar: types.Message):
    soat=await xabar.answer("⌛️")
    try:
        if xabar.text.startswith("https://www.instagram.com/"):
            url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"
            querystring = {"url": xabar.text}

            headers = {
              "X-RapidAPI-Key": "2f124f417amsh403faa005a2f2fdp171256jsneace865cbe92",
              "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring).json()

            await xabar.answer_video(video=response["media"],caption=response["title"])
        elif xabar.text.startswith("https://vm.tiktok.com/"):
            url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

            querystring = {"url": "https://vm.tiktok.com/ZS8Gn4Vow/"}

            headers = {
                "X-RapidAPI-Key": "eb59523282msh7afe13a2ccc53fdp181e6djsn7c4d816b692c",
                "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring).json()

            video = response['video'][0]
            music = response['music'][0]
            description = response['description'][0]
            await xabar.answer_video(video=video,caption=description)
            await xabar.answer_audio(music)
        elif xabar.text.startswith("https://youtu.be/"):
            url = "https://youtube-video-and-shorts-downloader.p.rapidapi.com/"

            querystring = {"url":xabar.text}

            headers = {
                "X-RapidAPI-Key": "eb59523282msh7afe13a2ccc53fdp181e6djsn7c4d816b692c",
                "X-RapidAPI-Host": "youtube-video-and-shorts-downloader.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            y=response.json()["video"][1]["url"]
            await  xabar.answer_video(y)
        elif xabar.text.startswith("https://www.facebook.com/"):
            url = "https://facebook-reel-and-video-downloader.p.rapidapi.com/app/main.php"

            querystring = {"url":xabar.text}

            headers = {
                "X-RapidAPI-Key": "eb59523282msh7afe13a2ccc53fdp181e6djsn7c4d816b692c",
                "X-RapidAPI-Host": "facebook-reel-and-video-downloader.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            q=response.json()["links"]['Download Low Quality']
            await xabar.answer(q)
        else:
            await xabar.answer("Siz faqat Instagram, Tik tok, Facebook va YouTube dan video yuklashingiz mumkin")
    except:
        await xabar.reply("linkda xatolik bor yaxshilab tekshiring")
    await soat.delete()
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)
