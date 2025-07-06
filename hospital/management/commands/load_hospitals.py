import csv
from django.core.management.base import BaseCommand
from hospital.models import Hospital

class Command(BaseCommand):
    help = 'CSV 파일로 병원 데이터를 일괄 등록합니다 (2000개 제한).'

    def handle(self, *args, **kwargs):
        try:
            with open('converted_hospital_data.csv', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                count = 0
                for row in reader:
                    if count >= 100:
                        break  # ✅ 100개까지만 등록
                    Hospital.objects.create(
                        name=row['name'],
                        city=row['city'],
                        district=row['district'],
                        address=row['address'],
                        phone=row['phone']
                    )
                    count += 1
                    if count % 200 == 0:
                        self.stdout.write(f"🔄 {count}개 등록 중...")

                self.stdout.write(self.style.SUCCESS(f"✅ 병원 {count}개 등록 완료!"))
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ 오류 발생: {e}"))
