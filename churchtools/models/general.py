from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel  # type: ignore


class LicenseSettings(BaseModel):
    hide_licensetab: str


class Config(BaseModel):
    _current_config_file: Optional[str] = None
    accept_datasecurity: Optional[bool] = None
    access_control_allow_credentials: Optional[bool] = None
    access_control_allow_origins: Optional[str] = None
    admin_ids: Optional[List[str]] = None
    admin_mail: Optional[str] = None
    admin_message: Optional[str] = None
    aiAssistantAvailable: Optional[bool] = None
    ai_description_available_generation_count: Optional[int] = None
    ai_description_available_generation_tests: Optional[int] = None
    ai_description_generation_count: Optional[int] = None
    ai_description_generation_enabled: Optional[bool] = None
    ai_description_total_generation_count: Optional[int] = None
    allowaiassistant: Optional[bool] = None
    allowcheckin: Optional[str] = None
    allowedcals: Optional[str] = None
    allowedclients: Optional[str] = None
    allowedresources: Optional[str] = None
    allowedservices: Optional[str] = None
    allowedstations: Optional[str] = None
    allowedsyncconnections: Optional[str] = None
    allowedsyncjobs: Optional[str] = None
    alloweduser: Optional[str] = None
    allowfinance: Optional[str] = None
    allowldap: Optional[str] = None
    allowoptigemsync: Optional[str] = None
    allowsync: Optional[str] = None
    alpha_book_affiliate_id: Optional[str] = None
    alpha_book_enabled: Optional[bool] = None
    app_security_request: Optional[bool] = None
    authorized_persons: Optional[str] = None
    brand: Optional[str] = None
    build: Optional[str] = None
    ccli_auto_reporting_enabled: Optional[bool] = None
    ccli_last_token_refresh: Optional[str] = None
    ccli_refresh_token: Optional[str] = None
    chatServer: Optional[str] = None
    chrome_active: Optional[str] = None
    chrome_binary: Optional[str] = None
    churchcal_active: Optional[bool] = None
    churchcal_css: Optional[str] = None
    churchcal_entries_last_days: Optional[int] = None
    churchcal_firstdayinweek: Optional[int] = None
    churchcal_maincalname: Optional[str] = None
    churchcal_name: Optional[str] = None
    churchcal_name_default: Optional[str] = None
    churchcal_sortcode: Optional[int] = None
    churchchat_allow_event_chat: Optional[bool] = None
    churchchat_allow_group_chat: Optional[bool] = None
    churchchat_allow_person_chat: Optional[bool] = None
    churchchat_delete_event_chat_after_x_days: Optional[int] = None
    churchchat_invite_ct_event_chat: Optional[bool] = None
    churchchat_invite_ct_group_chat: Optional[bool] = None
    churchchat_name: Optional[str] = None
    churchchat_name_default: Optional[str] = None
    churchchat_sortcode: Optional[int] = None
    churchchat_start_event_chat_before_x_days: Optional[int] = None
    churchchat_start_event_chat_for_calendars: Optional[str] = None
    churchchat_sync_user_id: Optional[int] = None
    churchcheckin_active: Optional[bool] = None
    churchcheckin_label_child: Optional[str] = None
    churchcheckin_label_parent: Optional[str] = None
    churchcheckin_label_standard: Optional[str] = None
    churchcheckin_name: Optional[str] = None
    churchcheckin_name_default: Optional[str] = None
    churchcheckin_sortcode: Optional[int] = None
    churchcheckin_tags: Optional[str] = None
    churchcustommodule_active: Optional[str] = None
    churchcustommodule_name: Optional[str] = None
    churchcustommodule_name_default: Optional[str] = None
    churchdb_active: Optional[bool] = None
    churchdb_archivedeletehistory: Optional[bool] = None
    churchdb_birthdaylist_station: Optional[str] = None
    churchdb_birthdaylist_status: Optional[str] = None
    churchdb_cleverreach_client_id: Optional[str] = None
    churchdb_cleverreach_client_secret: Optional[str] = None
    churchdb_cleverreach_connected: Optional[bool] = None
    churchdb_emailseparator: Optional[str] = None
    churchdb_groupnotchoosable: Optional[int] = None
    churchdb_home_lat: Optional[str] = None
    churchdb_home_lng: Optional[str] = None
    churchdb_mailchimp_apikey: Optional[str] = None
    churchdb_mailchimp_connected: Optional[bool] = None
    churchdb_mailjet_apikey: Optional[str] = None
    churchdb_mailjet_apisecret: Optional[str] = None
    churchdb_mailjet_connected: Optional[bool] = None
    churchdb_memberlist_station: Optional[str] = None
    churchdb_memberlist_status: Optional[str] = None
    churchdb_name: Optional[str] = None
    churchdb_name_default: Optional[str] = None
    churchdb_sendgroupmails: Optional[bool] = None
    churchdb_smspromote_apikey: Optional[str] = None
    churchdb_sortcode: Optional[int] = None
    churchfinance_active: Optional[bool] = None
    churchfinance_name: Optional[str] = None
    churchfinance_name_default: Optional[str] = None
    churchfinance_sortcode: Optional[int] = None
    churchgroup_active: Optional[bool] = None
    churchgroup_inmenu: Optional[bool] = None
    churchgroup_name: Optional[str] = None
    churchgroup_name_default: Optional[str] = None
    churchgroup_sortcode: Optional[str] = None
    churchreport_active: Optional[bool] = None
    churchreport_name: Optional[str] = None
    churchreport_name_default: Optional[str] = None
    churchreport_sortcode: Optional[int] = None
    churchresource_active: Optional[bool] = None
    churchresource_anonymize_for_public_user: Optional[bool] = None
    churchresource_entries_last_days: Optional[int] = None
    churchresource_name: Optional[str] = None
    churchresource_name_default: Optional[str] = None
    churchresource_send_emails: Optional[bool] = None
    churchresource_sortcode: Optional[int] = None
    churchservice_active: Optional[bool] = None
    churchservice_agendashowenumeration: Optional[bool] = None
    churchservice_ccli_token: Optional[str] = None
    churchservice_ccli_token_secret: Optional[str] = None
    churchservice_entries_last_days: Optional[int] = None
    churchservice_invite_persons: Optional[bool] = None
    churchservice_name: Optional[str] = None
    churchservice_name_default: Optional[str] = None
    churchservice_openservice_rememberdays: Optional[int] = None
    churchservice_reminderhours: Optional[int] = None
    churchservice_songwithcategoryasdir: Optional[bool] = None
    churchservice_sortcode: Optional[int] = None
    churchsync_active: Optional[bool] = None
    churchsync_inmenu: Optional[bool] = None
    churchsync_name: Optional[str] = None
    churchsync_name_default: Optional[str] = None
    churchsync_sortcode: Optional[str] = None
    churchwiki_active: Optional[bool] = None
    churchwiki_name: Optional[str] = None
    churchwiki_name_default: Optional[str] = None
    churchwiki_sortcode: Optional[int] = None
    cron_daily: Optional[datetime] = None
    cron_hour_8: Optional[datetime] = None
    cronjob_dbdump: Optional[bool] = None
    cronjob_delay: Optional[int] = None
    csrf_enabled: Optional[bool] = None
    currently_mail_sending: Optional[str] = None
    datasecurity_banner_enabled: Optional[bool] = None
    datasecurity_privacy_agreement_text: Optional[str] = None
    datasecurity_privacy_agreement_text_for_children: Optional[str] = None
    db_name: Optional[str] = None
    db_password: Optional[str] = None
    db_server: Optional[str] = None
    db_user: Optional[str] = None
    default_phone_area_code: Optional[str] = None
    emailServer: Optional[str] = None
    encryptionkey: Optional[str] = None
    env: Optional[str] = None
    evangelische_termine_api_key: Optional[str] = None
    evangelische_termine_enabled: Optional[bool] = None
    evangelische_termine_name: Optional[str] = None
    evangelische_termine_url: Optional[str] = None
    evangelische_termine_vid: Optional[str] = None
    feature_custommodule: Optional[str] = None
    feature_darkmode: Optional[str] = None
    feature_group: Optional[str] = None
    feature_sync: Optional[str] = None
    finance_active: Optional[bool] = None
    finance_inmenu: Optional[str] = None
    finance_name: Optional[str] = None
    finance_name_default: Optional[str] = None
    finance_sortcode: Optional[str] = None
    first_sync_job: Optional[datetime] = None
    first_transaction: Optional[datetime] = None
    hostingservice: Optional[str] = None
    https_only: Optional[str] = None
    image_extension: Optional[str] = None
    installation_verification_code: Optional[str] = None
    invite_email_text: Optional[str] = None
    isPostsActive: Optional[bool] = None
    isSamlActive: Optional[bool] = None
    is_churchtools_blog_widget_active: Optional[bool] = None
    is_churchtools_onboarding_widget_active: Optional[bool] = None
    is_pr_widget_active: Optional[bool] = None
    is_rss_widget_active: Optional[bool] = None
    language: Optional[str] = None
    last_cron: Optional[str] = None
    last_cron_finished: Optional[str] = None
    last_db_dump: Optional[str] = None
    last_import_clear: Optional[str] = None
    last_translation_update: Optional[str] = None
    ldap_otp_enabled: Optional[bool] = None
    licenseSettings: Optional[LicenseSettings] = None
    log_debug: Optional[str] = None
    login_message: Optional[str] = None
    mail_enabled: Optional[bool] = None
    mail_sending_in_background: Optional[str] = None
    mail_sending_starttime: Optional[str] = None
    mail_smtp_args_host: Optional[str] = None
    mail_smtp_args_password: Optional[str] = None
    mail_smtp_args_port: Optional[str] = None
    mail_smtp_args_smtpsecure: Optional[str] = None
    mail_smtp_args_username: Optional[str] = None
    max_uploadfile_size_kb: Optional[int] = None
    memberlist_birthday_full: Optional[str] = None
    memberlist_email: Optional[str] = None
    memberlist_fax: Optional[str] = None
    memberlist_group_couples: Optional[str] = None
    memberlist_picture: Optional[str] = None
    memberlist_salutation: Optional[str] = None
    memberlist_telefongeschaeftlich: Optional[str] = None
    memberlist_telefonhandy: Optional[str] = None
    memberlist_telefonprivat: Optional[str] = None
    onboarding_start: Optional[datetime] = None
    openstreetmaps_enabled: Optional[bool] = None
    orderstatus: Optional[str] = None
    orderstatus_since_date: Optional[datetime] = None
    package: Optional[str] = None
    post_active: Optional[bool] = None
    post_edit_time_limited: Optional[bool] = None
    post_email_summary_default_enabled: Optional[bool] = None
    post_featured_groups: Optional[str] = None
    post_name: Optional[str] = None
    post_sortcode: Optional[int] = None
    post_wizard_completed: Optional[bool] = None
    post_wizard_groups: Optional[str] = None
    prevent_change_security_settings: Optional[bool] = None
    prevent_export: Optional[bool] = None
    privacy_policy_external: Optional[bool] = None
    privacy_policy_external_link: Optional[str] = None
    privacy_policy_fields_mandatory: Optional[bool] = None
    privacy_policy_fields_not_mandatory_api: Optional[bool] = None
    privacy_policy_internal: Optional[bool] = None
    privacy_policy_relationships: Optional[str] = None
    profile: Optional[str] = None
    rabbitmq_config_host: Optional[str] = None
    rabbitmq_config_password: Optional[str] = None
    rabbitmq_config_port: Optional[str] = None
    rabbitmq_config_user: Optional[str] = None
    rss_widget_link: Optional[str] = None
    safe_mode_enable_authorized_persons: Optional[str] = None
    safe_mode_enable_chat_sync: Optional[str] = None
    safe_mode_enable_consolidation: Optional[str] = None
    safe_mode_enable_guid_sync: Optional[str] = None
    safe_mode_enable_job_queueing: Optional[str] = None
    safe_mode_enable_mail: Optional[str] = None
    safe_mode_enable_newsletter: Optional[str] = None
    safe_mode_enable_notification: Optional[str] = None
    send_data_security_mails: Optional[bool] = None
    short_name: Optional[str] = None
    show_remember_me: Optional[bool] = None
    site_language: Optional[str] = None
    site_licensekey: Optional[str] = None
    site_logo: Optional[str] = None
    site_mail: Optional[str] = None
    site_name: Optional[str] = None
    site_offline: Optional[bool] = None
    site_startpage: Optional[str] = None
    site_url: Optional[str] = None
    support_user_active_since: Optional[datetime] = None
    test: Optional[str] = None
    timezone: Optional[str] = None
    version: Optional[str] = None
    webchatLink: Optional[str] = None
    website_order_status: Optional[str] = None
    website_sync_user_id: Optional[str] = None
    website_trial_user_id: Optional[int] = None
    website_url: Optional[str] = None
    welcome: Optional[str] = None
    welcome_subtext: Optional[str] = None


class SearchResult(BaseModel):
    apiUrl: str
    domainIdentifier: str
    domainType: str
    frontendUrl: str
    icon: str
    imageUrl: Optional[str] = None
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
