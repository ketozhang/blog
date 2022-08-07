FROM jekyll/jekyll:4.2.0

WORKDIR /tmp
COPY Gemfile Gemfile.lock .
RUN bundle install && rm Gemfile Gemfile.lock

WORKDIR /srv/jekyll