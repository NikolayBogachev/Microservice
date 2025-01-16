import aiohttp
import asyncio
import json


async def create_application():
    url = "http://localhost:8000/applications"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "user_name": "JohnDoe",
        "description": "This is a test application created via aiohttp."
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            if response.status == 200:
                print(f"Application created successfully: {await response.text()}")
            else:
                print(f"Failed to create application. Status code: {response.status}")


async def get_applications_by_user(user_name: str):
    url = f"http://localhost:8000/applications?user_name={user_name}&page=1&size=10"

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                applications = await response.json()
                print(f"Applications for {user_name}: {json.dumps(applications, indent=4)}")
            else:
                print(f"Failed to fetch applications. Status code: {response.status}")



# Запускаем тест
# asyncio.run(create_application())


# Запускаем тест для пользователя "JohnDoe"
asyncio.run(get_applications_by_user("JohnDoe"))