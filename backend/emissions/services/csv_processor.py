import pandas as pd

from emissions.models import (
    Company,
    DataSource,
    EmissionRecord
)


SUSPICIOUS_THRESHOLD = 10000


def normalize_unit(value, unit):

    unit = unit.lower()

    conversion_factors = {
        'kg': 1,
        'ton': 1000,
        'tons': 1000
    }

    factor = conversion_factors.get(unit, 1)

    normalized_value = value * factor

    return normalized_value, 'kg'


def is_suspicious(value):

    return value > SUSPICIOUS_THRESHOLD


def process_csv(file_path, company_id, source_type):

    company = Company.objects.get(id=company_id)

    data_source = DataSource.objects.create(
        company=company,
        source_type=source_type,
        uploaded_file=file_path
    )

    df = pd.read_csv(file_path)

    for _, row in df.iterrows():

        raw_value = float(row['value'])

        raw_unit = row['unit']

        normalized_value, normalized_unit = normalize_unit(
            raw_value,
            raw_unit
        )

        suspicious = is_suspicious(
            normalized_value
        )

        EmissionRecord.objects.create(
            company=company,
            source=data_source,
            category=row['category'],
            record_type=row['record_type'],
            raw_value=raw_value,
            raw_unit=raw_unit,
            normalized_value=normalized_value,
            normalized_unit=normalized_unit,
            is_suspicious=suspicious
        )

    return True