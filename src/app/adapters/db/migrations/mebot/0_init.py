from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "chat" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" VARCHAR(128) NOT NULL DEFAULT 'False',
    "last_admins_update" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "chat_member" (
    "user_id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "chat_id" BIGINT NOT NULL,
    "is_admin" INT NOT NULL DEFAULT 0,
    "is_bot" INT NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztl19v2jAQwL8K4qmTugoCFLY36NjKVGBq6Ta1qiInMcGqY6ex0xZVfPfZToKTkKSgai"
    "2b+gS5P/bdz85d7qnuQYvyo5MF4PXPtac6AR4Uf9Liw1od+P5aKJ85sLAysxMDi/EA2HKN"
    "OcAMCpEDmR0gnyNKhJSEGEshtYUhIq4WhQTdhdDk1IV8AQOhuL4RYkQc+AhZ8ujfmnMEsZ"
    "MJEjlybyU3+dJXsgFyR4R/VbZyQ8u0KQ49ou39JV9QsnZARGXgQgIDwKHcgQehzEAGGCea"
    "JBUFq02iKFM+DpyDEPNUxltisCmRCEU0TOXoyl0+fjKMVqtrNFrHvU672+30Gj1hq0LaVH"
    "VXUcIaSLSUwjL6NprMZKJUnFN0eFKwUj6Ag8hL8daA1e8GYnErgmLAiX0OsUgsjzgBWsU4"
    "EWjI+m4llHe9bXnMHng0MSQuX4jHptGrQPizf35y2j8/EFYfsiAnscqIdJKpZogB4yZwPE"
    "SYGfoCdQHRL0LKkQeLqRavkGPsxEscJX/+FvEX3usAAmdK8DJ+ZSp4z0bj4cWsP/4hM/EY"
    "u8MKVX82lBpDSZc56cFx7mjWi9R+jWanNflYu5pOhoogZdwN1I7abnZVlzGBkFOT0AfBPf"
    "V2J9IkeFmZ5repV0cKLGDfPoDAMTc01KBltpsqz/DyEkCAq05FspVR6io9hp6limdRCY+V"
    "zxVy09N2b1LPQwYDc9einnJ6r+xbV3Z13ruiTjk9j3pP6s0r0k59mLCoXhfgpRRDQEq+T1"
    "JuOcCW8NvTHlpFazo9y1TvwSjHbnI5HgxFT1VlWxghXo40rlm7AY2d3nGu9qRb9WGA7EVB"
    "p4oVVV0KaJO9GTj+o2nDaLa77V7ruL0ujmtJVU18vtvcw4DJkDbglY8SKZfXmyZeSDEzTB"
    "idzhbDhLAqHSaULlsF5ZuxA8TY/N8E2Gw0tpnGGo3yaUzqsgDFjhySgj7y/WI6Kfnq0S45"
    "kJdEJHjtIJsf1jBi/GY/sVZQlFlnOkoC72Dc/53nenI2HeTnJrnA4K17y+oPLdrx4A=="
)
