from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel  # type: ignore


class LicenseSettings(BaseModel):
    hide_licensetab: str


class Config(BaseModel):
    _current_config_file: str
    accept_datasecurity: bool
    access_control_allow_credentials: bool
    access_control_allow_origins: str
    admin_ids: List[str]
    admin_mail: str
    admin_message: str
    aiAssistantAvailable: bool
    ai_description_available_generation_count: int
    ai_description_available_generation_tests: int
    ai_description_generation_count: int
    ai_description_generation_enabled: bool
    ai_description_total_generation_count: int
    allowaiassistant: bool
    allowcheckin: str
    allowedcals: str
    allowedclients: str
    allowedresources: str
    allowedservices: str
    allowedstations: str
    allowedsyncconnections: str
    allowedsyncjobs: str
    alloweduser: str
    allowfinance: str
    allowldap: Optional[str] = None
    allowoptigemsync: str
    allowsync: Optional[str] = None
    alpha_book_affiliate_id: Optional[str] = None
    alpha_book_enabled: bool
    app_security_request: bool
    authorized_persons: str
    brand: str
    build: str
    ccli_auto_reporting_enabled: bool
    ccli_last_token_refresh: Optional[str] = None
    ccli_refresh_token: Optional[str] = None
    chatServer: str
    chrome_active: str
    chrome_binary: str
    churchcal_active: bool
    churchcal_css: Optional[str] = None
    churchcal_entries_last_days: int
    churchcal_firstdayinweek: int
    churchcal_maincalname: str
    churchcal_name: str
    churchcal_name_default: str
    churchcal_sortcode: int
    churchchat_allow_event_chat: bool
    churchchat_allow_group_chat: bool
    churchchat_allow_person_chat: bool
    churchchat_delete_event_chat_after_x_days: int
    churchchat_invite_ct_event_chat: bool
    churchchat_invite_ct_group_chat: bool
    churchchat_name: str
    churchchat_name_default: str
    churchchat_sortcode: int
    churchchat_start_event_chat_before_x_days: Optional[int] = None
    churchchat_start_event_chat_for_calendars: Optional[str] = None
    churchchat_sync_user_id: int
    churchcheckin_active: bool
    churchcheckin_label_child: str
    churchcheckin_label_parent: str
    churchcheckin_label_standard: str
    churchcheckin_name: str
    churchcheckin_name_default: str
    churchcheckin_sortcode: int
    churchcheckin_tags: Optional[str] = None
    churchcustommodule_active: str
    churchcustommodule_name: str
    churchcustommodule_name_default: str
    churchdb_active: bool
    churchdb_archivedeletehistory: bool
    churchdb_birthdaylist_station: str
    churchdb_birthdaylist_status: str
    churchdb_cleverreach_client_id: Optional[str] = None
    churchdb_cleverreach_client_secret: Optional[str] = None
    churchdb_cleverreach_connected: Optional[bool] = None
    churchdb_emailseparator: str
    churchdb_groupnotchoosable: int
    churchdb_home_lat: str
    churchdb_home_lng: str
    churchdb_mailchimp_apikey: str
    churchdb_mailchimp_connected: Optional[bool] = None
    churchdb_mailjet_apikey: Optional[str] = None
    churchdb_mailjet_apisecret: Optional[str] = None
    churchdb_mailjet_connected: Optional[bool] = None
    churchdb_memberlist_station: str
    churchdb_memberlist_status: str
    churchdb_name: str
    churchdb_name_default: str
    churchdb_sendgroupmails: bool
    churchdb_smspromote_apikey: str
    churchdb_sortcode: int
    churchfinance_active: bool
    churchfinance_name: str
    churchfinance_name_default: str
    churchfinance_sortcode: int
    churchgroup_active: bool
    churchgroup_inmenu: bool
    churchgroup_name: str
    churchgroup_name_default: str
    churchgroup_sortcode: str
    churchreport_active: bool
    churchreport_name: str
    churchreport_name_default: str
    churchreport_sortcode: int
    churchresource_active: bool
    churchresource_anonymize_for_public_user: bool
    churchresource_entries_last_days: int
    churchresource_name: str
    churchresource_name_default: str
    churchresource_send_emails: bool
    churchresource_sortcode: int
    churchservice_active: bool
    churchservice_agendashowenumeration: bool
    churchservice_ccli_token: Optional[str] = None
    churchservice_ccli_token_secret: Optional[str] = None
    churchservice_entries_last_days: int
    churchservice_invite_persons: bool
    churchservice_name: str
    churchservice_name_default: str
    churchservice_openservice_rememberdays: int
    churchservice_reminderhours: int
    churchservice_songwithcategoryasdir: bool
    churchservice_sortcode: int
    churchsync_active: bool
    churchsync_inmenu: bool
    churchsync_name: str
    churchsync_name_default: str
    churchsync_sortcode: str
    churchwiki_active: bool
    churchwiki_name: str
    churchwiki_name_default: str
    churchwiki_sortcode: int
    cron_daily: datetime
    cron_hour_8: datetime
    cronjob_dbdump: bool
    cronjob_delay: int
    csrf_enabled: bool
    currently_mail_sending: str
    datasecurity_banner_enabled: bool
    datasecurity_privacy_agreement_text: Optional[str] = None
    datasecurity_privacy_agreement_text_for_children: Optional[str] = None
    db_name: str
    db_password: str
    db_server: str
    db_user: str
    default_phone_area_code: str
    emailServer: str
    encryptionkey: str
    env: Optional[str] = None
    evangelische_termine_api_key: Optional[str] = None
    evangelische_termine_enabled: bool
    evangelische_termine_name: str
    evangelische_termine_url: Optional[str] = None
    evangelische_termine_vid: Optional[str] = None
    feature_custommodule: Optional[str] = None
    feature_darkmode: Optional[str] = None
    feature_group: str
    feature_sync: Optional[str] = None
    finance_active: bool
    finance_inmenu: str
    finance_name: str
    finance_name_default: str
    finance_sortcode: str
    first_sync_job: Optional[datetime] = None
    first_transaction: datetime
    hostingservice: str
    https_only: str
    image_extension: Optional[str] = None
    installation_verification_code: Optional[str] = None
    invite_email_text: str
    isPostsActive: bool
    isSamlActive: bool
    is_churchtools_blog_widget_active: bool
    is_churchtools_onboarding_widget_active: bool
    is_pr_widget_active: bool
    is_rss_widget_active: bool
    language: str
    last_cron: str
    last_cron_finished: str
    last_db_dump: str
    last_import_clear: str
    last_translation_update: str
    ldap_otp_enabled: bool
    licenseSettings: Optional[LicenseSettings] = None
    log_debug: Optional[str] = None
    login_message: str
    mail_enabled: bool
    mail_sending_in_background: str
    mail_sending_starttime: str
    mail_smtp_args_host: str
    mail_smtp_args_password: str
    mail_smtp_args_port: str
    mail_smtp_args_smtpsecure: str
    mail_smtp_args_username: str
    max_uploadfile_size_kb: int
    memberlist_birthday_full: str
    memberlist_email: str
    memberlist_fax: str
    memberlist_group_couples: str
    memberlist_picture: str
    memberlist_salutation: str
    memberlist_telefongeschaeftlich: str
    memberlist_telefonhandy: str
    memberlist_telefonprivat: str
    onboarding_start: datetime
    openstreetmaps_enabled: bool
    orderstatus: str
    orderstatus_since_date: datetime
    package: str
    post_active: bool
    post_edit_time_limited: Optional[bool] = None
    post_email_summary_default_enabled: Optional[bool] = None
    post_featured_groups: Optional[str] = None
    post_name: str
    post_sortcode: int
    post_wizard_completed: bool
    post_wizard_groups: Optional[str] = None
    prevent_change_security_settings: Optional[bool] = None
    prevent_export: bool
    privacy_policy_external: bool
    privacy_policy_external_link: str
    privacy_policy_fields_mandatory: bool
    privacy_policy_fields_not_mandatory_api: Optional[bool] = None
    privacy_policy_internal: bool
    privacy_policy_relationships: str
    profile: str
    rabbitmq_config_host: str
    rabbitmq_config_password: str
    rabbitmq_config_port: str
    rabbitmq_config_user: str
    rss_widget_link: str
    safe_mode_enable_authorized_persons: Optional[str] = None
    safe_mode_enable_chat_sync: Optional[str] = None
    safe_mode_enable_consolidation: Optional[str] = None
    safe_mode_enable_guid_sync: Optional[str] = None
    safe_mode_enable_job_queueing: Optional[str] = None
    safe_mode_enable_mail: Optional[str] = None
    safe_mode_enable_newsletter: Optional[str] = None
    safe_mode_enable_notification: Optional[str] = None
    send_data_security_mails: bool
    short_name: str
    show_remember_me: bool
    site_language: str
    site_licensekey: str
    site_logo: str
    site_mail: str
    site_name: str
    site_offline: bool
    site_startpage: str
    site_url: str
    support_user_active_since: Optional[datetime] = None
    test: Optional[str] = None
    timezone: str
    version: str
    webchatLink: str
    website_order_status: str
    website_sync_user_id: str
    website_trial_user_id: Optional[int] = None
    website_url: str
    welcome: str
    welcome_subtext: str


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


class VersionInfo(BaseModel):
    build: str
    version: str

    def __repr__(self) -> str:
        return f"<Version: {self.version} (build: {self.build})>"
