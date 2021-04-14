from dateutil import parser


class Event:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.guid = qdict['guid'] if 'guid' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.description = qdict['description'] \
            if 'description' in qdict else None
        self.startDate = parser.parse(qdict['startDate']) \
            if 'startDate' in qdict else None
        self.endDate = parser.parse(qdict['endDate']) \
            if 'endDate' in qdict else None
        self.chatStatus = qdict['chatStatus'] \
            if 'chatStatus' in qdict else None
        # TODO: permissions
        # TODO: calendar

        self.eventServices = []
        if 'eventServices' in qdict:
            for s in qdict['eventServices']:
                self.eventServices.append(EventService(s))

    def __repr__(self):
        return f'<Event: {self.startDate.day:02}.' \
            f'{self.startDate.month:02} {self.startDate.hour:02}:' \
            f'{self.startDate.minute:02} "{self.name}">'


class EventService:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.personId = qdict['personId'] if 'personId' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.serviceId = qdict['serviceId'] if 'serviceId' in qdict else None
        self.agreed = qdict['agreed'] if 'agreed' in qdict else None
        self.isValid = qdict['isValid'] if 'isValid' in qdict else None
        self.requestedDate = qdict['requestedDate'] \
            if 'requestedDate' in qdict else None
        self.requesterPersonId = qdict['requesterPersonId'] \
            if 'requesterPersonId' in qdict else None
        self.comment = qdict['comment'] if 'comment' in qdict else None
        self.counter = qdict['counter'] if 'counter' in qdict else None
        self.allowChat = qdict['allowChat'] if 'allowChat' in qdict else None
        # TODO: person
        # TODO: requesterPerson


class Person:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.securityLevelForPerson = qdict['securityLevelForPerson'] \
            if 'securityLevelForPerson' in qdict else None
        self.editSecurityLevelForPerson = qdict['editSecurityLevelForPerson'] \
            if 'editSecurityLevelForPerson' in qdict else None
        self.title = qdict['title'] if 'title' in qdict else None
        self.firstName = qdict['firstName'] if 'firstName' in qdict else None
        self.lastName = qdict['lastName'] if 'lastName' in qdict else None
        self.nickname = qdict['nickname'] if 'nickname' in qdict else None
        self.job = qdict['job'] if 'job' in qdict else None
        self.street = qdict['street'] if 'street' in qdict else None
        self.addressAddition = qdict['addressAddition'] \
            if 'addressAddition' in qdict else None
        self.zip = qdict['zip'] if 'zip' in qdict else None
        self.city = qdict['city'] if 'city' in qdict else None
        self.country = qdict['country'] if 'country' in qdict else None
        self.latitude = qdict['latitude'] if 'latitude' in qdict else None
        self.longitude = qdict['longitude'] if 'longitude' in qdict else None
        self.latitudeLoose = qdict['latitudeLoose'] \
            if 'latitudeLoose' in qdict else None
        self.longitudeLoose = qdict['longitudeLoose'] \
            if 'longitudeLoose' in qdict else None
        self.phonePrivate = qdict['phonePrivate'] \
            if 'phonePrivate' in qdict else None
        self.phoneWork = qdict['phoneWork'] if 'phoneWork' in qdict else None
        self.mobile = qdict['mobile'] if 'mobile' in qdict else None
        self.fax = qdict['fax'] if 'fax' in qdict else None
        self.birthName = qdict['birthName'] if 'birthName' in qdict else None
        self.birthday = qdict['birthday'] if 'birthday' in qdict else None
        self.birthplace = qdict['birthplace'] \
            if 'birthplace' in qdict else None
        self.imageUrl = qdict['imageUrl'] if 'imageUrl' in qdict else None
        self.familyImageUrl = qdict['familyImageUrl'] \
            if 'familyImageUrl' in qdict else None
        self.sexId = qdict['sexId'] if 'sexId' in qdict else None
        self.email = qdict['email'] if 'email' in qdict else None
        self.cmsUserId = qdict['cmsUserId'] if 'cmsUserId' in qdict else None
        self.optigemId = qdict['optigemId'] if 'optigemId' in qdict else None
        self.privacyPolicyAgreement = \
            PrivacyPolicyAgreement(qdict['privacyPolicyAgreement']) \
            if 'privacyPolicyAgreement' in qdict else None
        self.nationalityId = qdict['nationalityId'] \
            if 'nationalityId' in qdict else None
        self.familyStatusId = qdict['familyStatusId'] \
            if 'familyStatusId' in qdict else None
        self.weddingDate = qdict['weddingDate'] \
            if 'weddingDate' in qdict else None
        self.campusId = qdict['campusId'] if 'campusId' in qdict else None
        self.statusId = qdict['statusId'] if 'statusId' in qdict else None
        self.departmentIds = qdict['departmentIds'] \
            if 'departmentIds' in qdict else None
        self.firstContact = qdict['firstContact'] \
            if 'firstContact' in qdict else None
        self.dateOfBelonging = qdict['dateOfBelonging'] \
            if 'dateOfBelonging' in qdict else None
        self.dateOfEntry = qdict['dateOfEntry'] \
            if 'dateOfEntry' in qdict else None
        self.dateOfResign = qdict['dateOfResign'] \
            if 'dateOfResign' in qdict else None
        self.dateOfBaptism = qdict['dateOfBaptism'] \
            if 'dateOfBaptism' in qdict else None
        self.placeOfBaptism = qdict['placeOfBaptism'] \
            if 'placeOfBaptism' in qdict else None
        self.baptisedBy = qdict['baptisedBy'] \
            if 'baptisedBy' in qdict else None
        self.referredBy = qdict['referredBy'] \
            if 'referredBy' in qdict else None
        self.referredTo = qdict['referredTo'] \
            if 'referredTo' in qdict else None
        self.growPathId = qdict['growPathId'] \
            if 'growPathId' in qdict else None
        self.isArchived = qdict['isArchived'] \
            if 'isArchived' in qdict else None
        self.meta = qdict['meta'] if 'meta' in qdict else None

    def __repr__(self):

        return f'<Person: {self.firstName} {self.lastName} [{self.id}]>'


class PersonDomainAttributes:

    def __init__(self, qdict):

        self.firstName = qdict['firstName'] if 'firstName' in qdict else None
        self.lastName = qdict['lastName'] if 'lastName' in qdict else None
        self.guid = qdict['guid'] if 'guid' in qdict else None

    def __repr__(self):

        return f'<PersonDomainAttributes "{self.firstName} {self.lastName}">'


class PersonDomainObject:

    def __init__(self, qdict):

        self.imageUrl = qdict['imageUrl'] if 'imageUrl' in qdict else None
        self.frontendUrl = qdict['frontendUrl'] \
            if 'frontendUrl' in qdict else None
        self.apiUrl = qdict['apiUrl'] if 'apiUrl' in qdict else None
        self.domainType = qdict['domainType'] \
            if 'domainType' in qdict else None
        self.title = qdict['title'] if 'title' in qdict else None
        self.domainIdentifier = qdict['domainIdentifier'] \
            if 'domainIdentifier' in qdict else None

        self.domainAttributes = PersonDomainAttributes(
            qdict['domainAttributes']) if 'domainAttributes' in qdict else None

    def __repr__(self):

        return f'<PersonDomainObject "{self.title}">'


class PersonRelationship:

    def __init__(self, qdict):

        self.relative = PersonDomainObject(qdict['relative']) \
            if 'relative' in qdict else None
        self.degreeOfRelationship = qdict['degreeOfRelationship'] \
            if 'degreeOfRelationship' in qdict else None
        self.relationshipName = qdict['relationshipName'] \
            if 'relationshipName' in qdict else None
        self.relationshipTypeId = qdict['relationshipTypeId'] \
            if 'relationshipTypeId' in qdict else None

    def __repr__(self):

        return f'<PersonRelationship: {self.relative.title} '\
            f'({self.degreeOfRelationship})>'


class PersonTag:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.count = qdict['count'] if 'count' in qdict else None

    def __repr__(self):

        return f'<PersonTag "{self.name}">'


class PrivacyPolicyAgreement:

    def __init__(self, qdict):

        self.date = qdict['date'] if 'date' in qdict else None
        self.typeId = qdict['typeId'] if 'typeId' in qdict else None
        self.whoId = qdict['whoId'] if 'whoId' in qdict else None


class Song:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.category = SongCategory(qdict['category']) \
            if 'category' in qdict else None
        self.shouldPractice = qdict['shouldPractice'] \
            if 'shouldPractice' in qdict else None
        self.author = qdict['author'] if 'author' in qdict else None
        self.ccli = qdict['ccli'] if 'ccli' in qdict else None
        self.copyright = qdict['copyright'] if 'copyright' in qdict else None
        self.note = qdict['note'] if 'note' in qdict else None
        # TODO: meta

        self.arrangements = []
        if 'arrangements' in qdict:
            for item in qdict['arrangements']:
                self.arrangements.append(SongArrangement(item))

    def __repr__(self):
        return f'<Song: {self.name} [{self.id}]>'


class SongArrangement:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.isDefault = qdict['isDefault'] if 'isDefault' in qdict else None
        self.keyOfArrangement = qdict['keyOfArrangement'] \
            if 'keyOfArrangement' in qdict else None
        self.bpm = qdict['bpm'] if 'bpm' in qdict else None
        self.beat = qdict['beat'] if 'beat' in qdict else None
        self.duration = qdict['duration'] if 'duration' in qdict else None
        self.note = qdict['note'] if 'note' in qdict else None
        self.links = qdict['links'] if 'links' in qdict else None
        # TODO: meta

        self.files = []
        if 'files' in qdict:
            for item in qdict['files']:
                self.files.append(SongFile(item))

    def __repr__(self):

        return f'<SongArrangement: {self.name}>'


class SongCategory:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.nameTranslated = qdict['nameTranslated'] \
            if 'nameTranslated' in qdict else None
        self.sortKey = qdict['sortKey'] if 'sortKey' in qdict else None
        self.campusId = qdict['campusId'] if 'campusId' in qdict else None

    def __repr__(self):

        return f'<SongCategory: {self.name}>'


class SongFile:

    def __init__(self, qdict):

        self.domainType = qdict['domainType'] \
            if 'domainType' in qdict else None
        self.domainId = qdict['domainId'] if 'domainId' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.filename = qdict['filename'] if 'filename' in qdict else None
        self.fileUrl = qdict['fileUrl'] if 'fileUrl' in qdict else None

    def __repr__(self):

        return f'<SongFile: {self.name}>'


class Service:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.serviceGroupId = qdict['serviceGroupId'] \
            if 'serviceGroupId' in qdict else None
        self.commentOnConfirmation = qdict['commentOnConfirmation'] \
            if 'commentOnConfirmation' in qdict else None
        self.sortKey = qdict['sortKey'] if 'sortKey' in qdict else None
        self.allowDecline = qdict['allowDecline'] \
            if 'allowDecline' in qdict else None
        self.allowExchange = qdict['allowExchange'] \
            if 'allowExchange' in qdict else None
        self.comment = qdict['comment'] if 'comment' in qdict else None
        self.standard = qdict['standard'] if 'standard' in qdict else None
        self.hidePersonName = qdict['hidePersonName'] \
            if 'hidePersonName' in qdict else None
        self.sendReminderMails = qdict['sendReminderMails'] \
            if 'sendReminderMails' in qdict else None
        self.sendServiceRequestMails = qdict['sendServiceRequestMails'] \
            if 'sendServiceRequestMails' in qdict else None
        self.allowControlLiveAgenda = qdict['allowControlLiveAgenda'] \
            if 'allowControlLiveAgenda' in qdict else None
        self.groupIds = qdict['groupIds'] if 'groupIds' in qdict else None
        self.tagIds = qdict['tagIds'] if 'tagIds' in qdict else None
        self.calTextTemplate = qdict['calTextTemplate'] \
            if 'calTextTemplate' in qdict else None
        self.allowChat = qdict['allowChat'] if 'allowChat' in qdict else None

    def __repr__(self):

        return f'<Service: {self.name}>'


class Status:

    def __init__(self, qdict):

        self.id = qdict['id'] if 'id' in qdict else None
        self.name = qdict['name'] if 'name' in qdict else None
        self.shorty = qdict['shorty'] if 'shorty' in qdict else None
        self.isMember = qdict['isMember'] if 'isMember' in qdict else None
        self.isSearchable = qdict['isSearchable'] \
            if 'isSearchable' in qdict else None
        self.sortKey = qdict['sortKey'] if 'sortKey' in qdict else None
        self.securityLevelId = qdict['securityLevelId'] \
            if 'securityLevelId' in qdict else None

    def __repr__(self):

        return f'<Status: {self.name} [{self.id}]>'


class VersionInfo:

    def __init__(self, qdict):

        self.build = qdict['build'] if 'build' in qdict else None
        self.version = qdict['version'] if 'version' in qdict else None

    def __repr__(self):

        return f'<Version {self.version}>'
