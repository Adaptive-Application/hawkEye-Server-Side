from rest_framework import serializers
from .models import userPreference, userSubPreference


class PreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = userPreference
        fields = ('userId', 'preferenceCode', 'preferenceScore')

    def create(self, validated_data):
        username = validated_data.pop('username')
        data = validated_data.pop('data')
        preference = []
        for p in data['userpref']:
            pref = userPreference.objects.create(userId=username, preferenceCode=p['category']['code'],
                                                 preferenceScore=p['category']['score'])
            preference.append(pref)
        return preference

    def update(self, instance, validated_data):
        username = validated_data.pop('username')
        data = validated_data.pop('data')
        updatecount = []
        for p in data['userpref']:
            pref = instance.objects.filter(userId=username, preferenceCode=p['category']['code']). \
                update(preferenceScore=p['category']['score'])
            updatecount.append(pref)
        return updatecount


class SubPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSubPreference
        fields = ('userpreference_FK', 'subpreferenceCode', 'subpreferenceScore')

    def create(self, validated_data):
        username = validated_data.pop('username')
        data = validated_data.pop('data')
        preference = []
        for p in data['usersubpref']:
            inst = userPreference.objects.get(userId=username, preferenceCode=p['parent'])
            for sp in p['subcategory']:
                print(sp)
                pref = userSubPreference.objects.create(userpreference_FK=inst, subpreferenceCode=sp['code'],
                                                        subpreferenceScore=sp['score'])
                preference.append(pref)
        return preference

    def update(self, instance, validated_data):
        username = validated_data.pop('username')
        data = validated_data.pop('data')
        updatecount = []
        for p in data['usersubpref']:
            inst = userPreference.objects.get(userId=username, preferenceCode=p['parent'])
            for sp in p['subcategory']:
                pref = instance.objects.filter(userpreference_FK=inst, subpreferenceCode=sp['code']). \
                    update(subpreferenceScore=sp['score'])
                updatecount.append(pref)
        return updatecount
