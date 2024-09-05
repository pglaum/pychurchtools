from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel  # type: ignore


class LicenseSettings(BaseModel):
    hide_licensetab: str


class Config(BaseModel):
    _current_config_file: str | None = None
    accept_datasecurity: bool | None = None
    access_control_allow_credentials: bool | None = None
    access_control_allow_origins: str | None = None
    admin_ids: list[str] | None = None
    admin_mail: str | None = None
    admin_message: str | None = None
    aiAssistantAvailable: bool | None = None
    ai_description_available_generation_count: int | None = None
    ai_description_available_generation_tests: int | None = None
    ai_description_generation_count: int | None = None
    ai_description_generation_enabled: bool | None = None
    ai_description_total_generation_count: int | None = None
    allowaiassistant: bool | None = None
    allowcheckin: str | None = None
    allowedcals: str | None = None
    allowedclients: str | None = None
    allowedresources: str | None = None
    allowedservices: str | None = None
    allowedstations: str | None = None
    allowedsyncconnections: str | None = None
    allowedsyncjobs: str | None = None
    alloweduser: str | None = None
    allowfinance: str | None = None
    allowldap: str | None = None
    allowoptigemsync: str | None = None
    allowsync: str | None = None
    alpha_book_affiliate_id: str | None = None
    alpha_book_enabled: bool | None = None
    app_security_request: bool | None = None
    authorized_persons: str | None = None
    brand: str | None = None
    build: str | None = None
    ccli_auto_reporting_enabled: bool | None = None
    ccli_last_token_refresh: str | None = None
    ccli_refresh_token: str | None = None
    chatServer: str | None = None
    chrome_active: str | None = None
    chrome_binary: str | None = None
    churchcal_active: bool | None = None
    churchcal_css: str | None = None
    churchcal_entries_last_days: int | None = None
    churchcal_firstdayinweek: int | None = None
    churchcal_maincalname: str | None = None
    churchcal_name: str | None = None
    churchcal_name_default: str | None = None
    churchcal_sortcode: int | None = None
    churchchat_allow_event_chat: bool | None = None
    churchchat_allow_group_chat: bool | None = None
    churchchat_allow_person_chat: bool | None = None
    churchchat_delete_event_chat_after_x_days: int | None = None
    churchchat_invite_ct_event_chat: bool | None = None
    churchchat_invite_ct_group_chat: bool | None = None
    churchchat_name: str | None = None
    churchchat_name_default: str | None = None
    churchchat_sortcode: int | None = None
    churchchat_start_event_chat_before_x_days: int | None = None
    churchchat_start_event_chat_for_calendars: str | None = None
    churchchat_sync_user_id: int | None = None
    churchcheckin_active: bool | None = None
    churchcheckin_label_child: str | None = None
    churchcheckin_label_parent: str | None = None
    churchcheckin_label_standard: str | None = None
    churchcheckin_name: str | None = None
    churchcheckin_name_default: str | None = None
    churchcheckin_sortcode: int | None = None
    churchcheckin_tags: str | None = None
    churchcustommodule_active: str | None = None
    churchcustommodule_name: str | None = None
    churchcustommodule_name_default: str | None = None
    churchdb_active: bool | None = None
    churchdb_archivedeletehistory: bool | None = None
    churchdb_birthdaylist_station: str | None = None
    churchdb_birthdaylist_status: str | None = None
    churchdb_cleverreach_client_id: str | None = None
    churchdb_cleverreach_client_secret: str | None = None
    churchdb_cleverreach_connected: bool | None = None
    churchdb_emailseparator: str | None = None
    churchdb_groupnotchoosable: int | None = None
    churchdb_home_lat: str | None = None
    churchdb_home_lng: str | None = None
    churchdb_mailchimp_apikey: str | None = None
    churchdb_mailchimp_connected: bool | None = None
    churchdb_mailjet_apikey: str | None = None
    churchdb_mailjet_apisecret: str | None = None
    churchdb_mailjet_connected: bool | None = None
    churchdb_memberlist_station: str | None = None
    churchdb_memberlist_status: str | None = None
    churchdb_name: str | None = None
    churchdb_name_default: str | None = None
    churchdb_sendgroupmails: bool | None = None
    churchdb_smspromote_apikey: str | None = None
    churchdb_sortcode: int | None = None
    churchfinance_active: bool | None = None
    churchfinance_name: str | None = None
    churchfinance_name_default: str | None = None
    churchfinance_sortcode: int | None = None
    churchgroup_active: bool | None = None
    churchgroup_inmenu: bool | None = None
    churchgroup_name: str | None = None
    churchgroup_name_default: str | None = None
    churchgroup_sortcode: str | None = None
    churchreport_active: bool | None = None
    churchreport_name: str | None = None
    churchreport_name_default: str | None = None
    churchreport_sortcode: int | None = None
    churchresource_active: bool | None = None
    churchresource_anonymize_for_public_user: bool | None = None
    churchresource_entries_last_days: int | None = None
    churchresource_name: str | None = None
    churchresource_name_default: str | None = None
    churchresource_send_emails: bool | None = None
    churchresource_sortcode: int | None = None
    churchservice_active: bool | None = None
    churchservice_agendashowenumeration: bool | None = None
    churchservice_ccli_token: str | None = None
    churchservice_ccli_token_secret: str | None = None
    churchservice_entries_last_days: int | None = None
    churchservice_invite_persons: bool | None = None
    churchservice_name: str | None = None
    churchservice_name_default: str | None = None
    churchservice_openservice_rememberdays: int | None = None
    churchservice_reminderhours: int | None = None
    churchservice_songwithcategoryasdir: bool | None = None
    churchservice_sortcode: int | None = None
    churchsync_active: bool | None = None
    churchsync_inmenu: bool | None = None
    churchsync_name: str | None = None
    churchsync_name_default: str | None = None
    churchsync_sortcode: str | None = None
    churchwiki_active: bool | None = None
    churchwiki_name: str | None = None
    churchwiki_name_default: str | None = None
    churchwiki_sortcode: int | None = None
    cron_daily: datetime | None = None
    cron_hour_8: datetime | None = None
    cronjob_dbdump: bool | None = None
    cronjob_delay: int | None = None
    csrf_enabled: bool | None = None
    currently_mail_sending: str | None = None
    datasecurity_banner_enabled: bool | None = None
    datasecurity_privacy_agreement_text: str | None = None
    datasecurity_privacy_agreement_text_for_children: str | None = None
    db_name: str | None = None
    db_password: str | None = None
    db_server: str | None = None
    db_user: str | None = None
    default_phone_area_code: str | None = None
    emailServer: str | None = None
    encryptionkey: str | None = None
    env: str | None = None
    evangelische_termine_api_key: str | None = None
    evangelische_termine_enabled: bool | None = None
    evangelische_termine_name: str | None = None
    evangelische_termine_url: str | None = None
    evangelische_termine_vid: str | None = None
    feature_custommodule: str | None = None
    feature_darkmode: str | None = None
    feature_group: str | None = None
    feature_sync: str | None = None
    finance_active: bool | None = None
    finance_inmenu: str | None = None
    finance_name: str | None = None
    finance_name_default: str | None = None
    finance_sortcode: str | None = None
    first_sync_job: datetime | None = None
    first_transaction: datetime | None = None
    hostingservice: str | None = None
    https_only: str | None = None
    image_extension: str | None = None
    installation_verification_code: str | None = None
    invite_email_text: str | None = None
    isPostsActive: bool | None = None
    isSamlActive: bool | None = None
    is_churchtools_blog_widget_active: bool | None = None
    is_churchtools_onboarding_widget_active: bool | None = None
    is_pr_widget_active: bool | None = None
    is_rss_widget_active: bool | None = None
    language: str | None = None
    last_cron: str | None = None
    last_cron_finished: str | None = None
    last_db_dump: str | None = None
    last_import_clear: str | None = None
    last_translation_update: str | None = None
    ldap_otp_enabled: bool | None = None
    licenseSettings: LicenseSettings | None = None
    log_debug: str | None = None
    login_message: str | None = None
    mail_enabled: bool | None = None
    mail_sending_in_background: str | None = None
    mail_sending_starttime: str | None = None
    mail_smtp_args_host: str | None = None
    mail_smtp_args_password: str | None = None
    mail_smtp_args_port: str | None = None
    mail_smtp_args_smtpsecure: str | None = None
    mail_smtp_args_username: str | None = None
    max_uploadfile_size_kb: int | None = None
    memberlist_birthday_full: str | None = None
    memberlist_email: str | None = None
    memberlist_fax: str | None = None
    memberlist_group_couples: str | None = None
    memberlist_picture: str | None = None
    memberlist_salutation: str | None = None
    memberlist_telefongeschaeftlich: str | None = None
    memberlist_telefonhandy: str | None = None
    memberlist_telefonprivat: str | None = None
    onboarding_start: datetime | None = None
    openstreetmaps_enabled: bool | None = None
    orderstatus: str | None = None
    orderstatus_since_date: datetime | None = None
    package: str | None = None
    post_active: bool | None = None
    post_edit_time_limited: bool | None = None
    post_email_summary_default_enabled: bool | None = None
    post_featured_groups: str | None = None
    post_name: str | None = None
    post_sortcode: int | None = None
    post_wizard_completed: bool | None = None
    post_wizard_groups: str | None = None
    prevent_change_security_settings: bool | None = None
    prevent_export: bool | None = None
    privacy_policy_external: bool | None = None
    privacy_policy_external_link: str | None = None
    privacy_policy_fields_mandatory: bool | None = None
    privacy_policy_fields_not_mandatory_api: bool | None = None
    privacy_policy_internal: bool | None = None
    privacy_policy_relationships: str | None = None
    profile: str | None = None
    rabbitmq_config_host: str | None = None
    rabbitmq_config_password: str | None = None
    rabbitmq_config_port: str | None = None
    rabbitmq_config_user: str | None = None
    rss_widget_link: str | None = None
    safe_mode_enable_authorized_persons: str | None = None
    safe_mode_enable_chat_sync: str | None = None
    safe_mode_enable_consolidation: str | None = None
    safe_mode_enable_guid_sync: str | None = None
    safe_mode_enable_job_queueing: str | None = None
    safe_mode_enable_mail: str | None = None
    safe_mode_enable_newsletter: str | None = None
    safe_mode_enable_notification: str | None = None
    send_data_security_mails: bool | None = None
    short_name: str | None = None
    show_remember_me: bool | None = None
    site_language: str | None = None
    site_licensekey: str | None = None
    site_logo: str | None = None
    site_mail: str | None = None
    site_name: str | None = None
    site_offline: bool | None = None
    site_startpage: str | None = None
    site_url: str | None = None
    support_user_active_since: datetime | None = None
    test: str | None = None
    timezone: str | None = None
    version: str | None = None
    webchatLink: str | None = None
    website_order_status: str | None = None
    website_sync_user_id: str | None = None
    website_trial_user_id: int | None = None
    website_url: str | None = None
    welcome: str | None = None
    welcome_subtext: str | None = None


class SearchResult(BaseModel):
    apiUrl: str
    domainIdentifier: str
    domainType: str
    frontendUrl: str
    icon: str
    imageUrl: str | None = None
    title: str

    # TODO: domainAttributes

    def __repr__(self) -> str:
        return f"<SearchResult: {self.title} [{self.domainType}]>"


class SimulateStop(BaseModel):
    redirect: str


class VersionInfo(BaseModel):
    build: str
    shortName: str
    siteName: str
    version: str

    def __repr__(self) -> str:
        return f"<Version: {self.version} (build: {self.build})>"
