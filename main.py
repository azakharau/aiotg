from aiohttp import web

import settings


if __name__ == '__main__':
    app = web.Application()
    app['config'] = settings
    web.run_app(app)
