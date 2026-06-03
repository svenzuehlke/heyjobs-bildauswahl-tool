#!/usr/bin/env python3
"""
HeyJobs Bildkopier-Script mit Support für schlechte Bilder
Kopiert ausgewählte Bilder und schlechte Bilder für ML-Training
"""

import os
import csv
import shutil
from pathlib import Path

def main():
    print("=" * 60)
    print("HeyJobs - Bildkopier-Script")
    print("=" * 60)
    
    # CSV für ausgewählte Bilder
    csv_file = 'job_image_selections.csv'
    bad_csv_file = 'bad_images.csv'
    
    if not os.path.exists(csv_file):
        print(f"❌ {csv_file} nicht gefunden!")
        print("Bitte zuerst CSV aus dem Tool exportieren.")
        return
    
    # Zielordner erstellen
    base_dir = Path('final')
    bad_dir = Path('bad_images')
    
    categories = {
        'junger_deutsche': base_dir / 'junger_deutsche',
        'junge_deutsche': base_dir / 'junge_deutsche',
        'ältere_deutsche': base_dir / 'ältere_deutsche',
        'nicht_deutsch': base_dir / 'nicht_deutsch'
    }
    
    for folder in categories.values():
        folder.mkdir(parents=True, exist_ok=True)
        print(f"✓ {folder}")
    
    # Bad images Ordner
    bad_categories = {
        'junger_deutsche': bad_dir / 'junger_deutsche',
        'junge_deutsche': bad_dir / 'junge_deutsche',
        'ältere_deutsche': bad_dir / 'ältere_deutsche',
        'nicht_deutsch': bad_dir / 'nicht_deutsch'
    }
    
    for folder in bad_categories.values():
        folder.mkdir(parents=True, exist_ok=True)
        print(f"✓ {folder}")
    
    print()
    
    # Quellordner
    source_folders = {
        'junger_deutsche': 'junger_deutsche',
        'junge_deutsche': 'junge_deutsche',
        'ältere_deutsche': 'ältere_deutsche',
        'nicht_deutsch': 'nicht_deutsch'
    }
    
    copied_count = 0
    error_count = 0
    
    # Ausgewählte Bilder kopieren
    print("📋 Kopiere ausgewählte Bilder...")
    print()
    
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            job_id = row['Job-ID']
            job_title = row['Jobtitel']
            
            print(f"📋 Job {job_id}: {job_title}")
            
            for cat_key, cat_name in [
                ('Junger deutscher Mann', 'junger_deutsche'),
                ('Junge deutsche Frau', 'junge_deutsche'),
                ('Ältere deutsche Person', 'ältere_deutsche'),
                ('Nicht-deutsche Person', 'nicht_deutsch')
            ]:
                filename = row[cat_key]
                source_path = Path(source_folders[cat_name]) / filename
                dest_path = categories[cat_name] / filename
                
                try:
                    if source_path.exists():
                        shutil.copy2(source_path, dest_path)
                        print(f"  ✓ {cat_name}: {filename}")
                        copied_count += 1
                    else:
                        print(f"  ⚠️ Nicht gefunden: {source_path}")
                        error_count += 1
                except Exception as e:
                    print(f"  ❌ {filename}: {e}")
                    error_count += 1
            
            print()
    
    # Schlechte Bilder kopieren
    bad_count = 0
    if os.path.exists(bad_csv_file):
        print("🚩 Kopiere schlechte Bilder für Training...")
        print()
        
        with open(bad_csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                job_id = row['Job-ID']
                filename = row['Bildname']
                folder = row['Ordner']
                
                source_path = Path(folder) / filename
                dest_path = bad_categories[folder] / filename
                
                try:
                    if source_path.exists():
                        shutil.copy2(source_path, dest_path)
                        print(f"  🚩 {folder}: {filename}")
                        bad_count += 1
                    else:
                        print(f"  ⚠️ Nicht gefunden: {source_path}")
                except Exception as e:
                    print(f"  ❌ {filename}: {e}")
        
        print()
    
    print("=" * 60)
    print(f"✅ {copied_count} Bilder kopiert")
    print(f"🚩 {bad_count} schlechte Bilder für Training kopiert")
    if error_count > 0:
        print(f"⚠️ {error_count} Fehler")
    print(f"📁 Ausgewählte Bilder: {base_dir.absolute()}")
    print(f"📁 Schlechte Bilder: {bad_dir.absolute()}")
    print("=" * 60)

if __name__ == '__main__':
    main()
