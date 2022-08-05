IMAGE=jekyll/jekyll:4.2.0
local:
	docker run --rm -it -v ${PWD}:/srv/jekyll -p 4000:4000 ${IMAGE} jekyll serve

build:
	docker run --rm -it -v ${PWD}:/srv/jekyll ${IMAGE} jekyll build