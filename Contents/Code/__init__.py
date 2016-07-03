TITLE = 'Qmusic'
PREFIX = '/video/qmusicnl'
ICON = 'icon-default.jpg'
ART = 'art-default.jpg'

STREAM_URL = 'http://ooyalahd2-f.akamaihd.net/i/depers01_delivery@380042/master.m3u8'

####################################################################################################
def Start():

	HTTP.CacheTime = 0

	ObjectContainer.art = R(ART)
	ObjectContainer.title1 = TITLE

	VideoClipObject.art = R(ART)
	VideoClipObject.thumb = R(ICON)

####################################################################################################
@handler(PREFIX, TITLE, thumb=ICON, art=ART)
def MainMenu():

	oc = ObjectContainer()

	oc.add(CreateVideoClipObject(
		title = 'Qmusic Live',
		url = STREAM_URL
	))

	return oc

####################################################################################################
@route(PREFIX + '/createvideoclipobject', include_container=bool)
def CreateVideoClipObject(title, url, include_container=False, **kwargs):

	videoclip_obj = VideoClipObject(
		key = Callback(CreateVideoClipObject, title=title, url=url, include_container=True),
		rating_key = url,
		title = title,
		items = [
			MediaObject(
				parts = [
					PartObject(key=HTTPLiveStreamURL(url))
				],
				audio_channels = 2,
				optimized_for_streaming = True,
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[videoclip_obj])
	else:
		return videoclip_obj
