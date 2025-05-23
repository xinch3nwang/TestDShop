DEFAULTS = {
    # 站点基本设置
    'SITE_ID': 1,
    'SITE_TITLE': 'BaykeShop',
    'SITE_HEADER': 'baykeShop开源商城系统',
    'INDEX_TITLE': '欢迎使用BaykeShop商城系统',
    'DESCRIPTION': '基于Django构建的开源商城系统',
    'KEYWORDS': 'baykeShop,商城系统,Django商城系统,Django商城',
    'COPYRIGHT': 'BaykeShop © 2024 All rights reserved.',
    'ICP': '陕ICP备19000001号',

    # 邮箱基本配置
    'EMAIL_HOST': 'smtp.qq.com',
    'EMAIL_HOST_USER': '',
    'EMAIL_HOST_PASSWORD': '',
    'EMAIL_PORT': 465,
    'EMAIL_USE_SSL': True,
    'EMAIL_USE_TLS': False,
    'EMAIL_BACKEND': 'django.core.mail.backends.smtp.EmailBackend',
    'DEFAULT_FROM_EMAIL': '',
    'EMAIL_SUBJECT_PREFIX': '[baykeShop]',

    # 支付宝配置
    'ALIPAY_APPID': '2021000122666025',
    'ALIPAY_PRIVATE_KEY': 'MIIEogIBAAKCAQEAm3zZGqRtgBpbAY1f4eaHqwCycWOf1hvRbp/xfnb5HeIzyE5s2y+/Hbfl1c32ZvXczUCwo1UqI8LS+FUn4q0Knn+RBoQqrFKCJpfLR3IsYbBA02aXPt3H8QKIEBtDsEAeOmCj1/zuVzO9Wi81FTzKe9nkeSV4OV75M715oCwyfZg1vbESA0wQXXoE7B9t5Q2tyba2RNpHhhs8Blto/Q+2oayxUwHcOsrTZVLrIZeI2Rayt02WokaWx11ENUYbgY0eV12PgXRRbqYxsoIBJE14q49a9nrN12q8Vq1DvhCy9Ma4j/7ZTZEiN5oxha+DxRlk5KJ4y7IswViMwc/BRjC0bwIDAQABAoIBABTXsn6Ixgji/4oAunacoVkB2emrMhTQW82ZcRTDu/cOiGR0ZtEm4FaKfSug1UPN91AoOMVcOC7dAcy6FYOkMIU4kmcuNk4tLTchJ+Wm314k8zujR+jsb83VyglmrjclEShAJhZg2E4mKF67b0EuifH6Lk8y/5+pJHyUDIa1BfuhwystbzTeNCEAOQQ1CF/wPnOul8v9k1xXwxpvFDYUxBQGLPXsdPyqJixzGviuOgZA7zjROUHi14VWUbYnCOtvJsezTtr9BWm9evMYNDsCMOjozovM0uiZkQAJk0TgtBjW3xAzUa/XQLb3AlcKvUjGhu5RLcxQpLD7X75eUgjDkLECgYEAyyMX3SiqQkpfyJe4TJBUPCD3ddwpdAGa9Xh9Q6jGO1tAI7ytLfbNYp+8MPAR8QsQO0hW5F4PaANHfosGuP11AvO0HwLYDZI67LNXN1+cSE7Jj3iwOqPXMxxP2UgY3xSzfceD4VVJlqN8UraXY7iWVnn7ConeRzhysFtW1StOZLcCgYEAw/NfSv33tiTtICNjEA0qjmxO5pSnK6QdcmewM5MHAdo3uL3VT1JwlGSwLxUiFiTz61UwvgHFqxMPiN0xVkNmZsfB19GE2n7hgHws/k13Ow3WzLoLElRYetCgSNk4wOsIa9qQxOG59s9AP1IyBYuKjdLi/Z1JggBfU64gjmpkJgkCgYAFp1Ris18JuUgxLQfUGbA+fCxm+1msAN9vNYtG9suNm1yNohKv1M6ikA+MzSGys7wf6kOA151WJ8E1pGjrfSJkkqPQuSOKPSemrtcek2qmGItDkvhUqXqz0XXndjo6+ziDp6nj+5uwtZwgMTTFcb29ameyQ2QMV2XZwrEH/cyQwQKBgAHP2Eu7OXUntkGb0iit1nzmp3weV8VhiRwrtUdkzqXHvMgqiTRokL3uiGqHCX+m69J7QS4gmhFQ5c3gLbqceO/uXO5/83iJv9AOVeQsFzQmlpviBIQw33iTQUgrKgkuoy9MIBaR98Q+elubiPbgKXHSR2MM90cKddcyPv7SIQbxAoGAQLpY5hRKQ6Pnz8T27eO900F4iYDmIKbodUtiKPrEiZ/PN1bmxwrZ5m81t6ukuLZ2kra0ukeepwxzmLOGl3ZDKeKVD0VyUuegdNfOTBEnnEn3nz/Yz9HC6DoLVp/oop0ROwiMrxBg8EpYbG2Qgru9DA5KaWiiJb0EO2U7fO//SNE=',
    'ALIPAY_PUBLIC_KEY': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnGm4s+aI1LsCwL9i67GSqEICxqfkyzydk6TIA57M9++EHBUAsXHa5mpgUIQwlYKetzsdPnYK8rS7Pkn6RFogF639zoaRBIpCu8K/lazUB2PqykLdV+XH8DqtH3k6lz1hFRAOHDIn3wVqIUOC0H/G4TFsp8Cd/cgLYAFr12Fgm20/OW8GZNnhfZmmcbHc4el9CqWuEt1xRQLAgLiaDjTZ5RrgSwHem2p1kYKjcs0jw1M+IyKIZK0k6s/KwwqsSlG28ysP94nBI1v3vSIL0e25rvv5irYXi78hfmmO8+sBdYxBzkaF7tndTctTxTYMcnk/+1jKijahDW/72zTI0AwSxwIDAQAB',

    # 手机号验证规则
    'REGEX_PHONE' : r'^1[3-9]\d{9}$',
    # 上传图片大小
    'MAX_IMAGE_SIZE': 2 * 1024 * 1024,
    # 自定义菜单开关
    'USE_MENU': False,
}

IMPORT_STRINGS = [
    'EMAIL_BACKEND'
]

REMOVED_SETTINGS = []