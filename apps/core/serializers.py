from rest_framework import serializers

class SerializerBase(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field_name, field in self.fields.items():
            if isinstance(field, serializers.PrimaryKeyRelatedField):
                value = getattr(instance, field_name)
                if value is not None:
                    data[field_name] = str(value)
            elif isinstance(field, serializers.ManyRelatedField):
                data[field_name] = [str(value) for value in getattr(instance, field_name).all()]
        data["instance"] = str(instance)
        return data