sidekiq_config = {
    url:       'redis://localhost:6379/0',
    namespace: "app::sidekiq_#{Rails.env}"
}

Sidekiq.configure_server do |config|
  config.redis = sidekiq_config
end

Sidekiq.configure_client do |config|
  config.redis = sidekiq_config
end