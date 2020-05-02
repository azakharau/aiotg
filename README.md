# Telegram Bot API implementation

Asynchronous web server based on aiohttp and using Telegram Web API. 

Can works in two modes:
* longpooling (specify like debug mode)
* webhook (specify like production mode)


TODO
-----------
- [x] Infrastructure design.
- [x] Data models design.
- [x] Library design
- [ ] Controllers design.
- [ ] Routes design.
- [ ] Include aiopg into project.
- [ ] Needed helpers: 
  - [ ] DB init.
  - [ ] Debug run with longpooling.
- [ ] Logging subsystem.
- [ ] Telegram API methods asynchronous wrapper
- [ ] Bot implementations based on custom library
