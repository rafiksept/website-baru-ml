from celery import shared_task
import time
from celery import Celery
from datetime import timedelta, datetime
from celery.utils.log import get_task_logger
from dashboard.models import JumlahKendaraan
import random
from task.tl import record_and_annotate_vehicles


logger = get_task_logger(__name__)


celery = Celery(__name__)
celery.config_from_object(__name__)

@shared_task
def object_detection1():
    try : 
        streets = [
          {
            "street_name": "Jl. Kawi Arah Barat (BRI Kawi)",
            "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/244729190133053856685781.m3u8?token=null",
            "start_x": 422,
            "start_y": 371,
            "end_x": 847,
            "end_y": 272
        }
        ]

        street = streets[0] 
        day_period = "morning" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def object_detection2():
    try : 
        streets = [
          {
                "street_name": "Jl. Kawi Arah Timur (BRI Kawi)",
                "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/269060901340905226381917.m3u8?token=null",
                "start_x": 380,
                "start_y": 410,
                "end_x": 1000,
                "end_y": 720
            }
        ]

        street = streets[0] 
        day_period = "morning" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def object_detection3():
    try : 
        streets = [
        {
            "street_name": "Jl. Kawi Arah Utara (BRI Kawi)",
            "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/599118267175295987908194.m3u8?token=null",
            "start_x": 736,
            "start_y": 187,
            "end_x": 1033,
            "end_y":202
        }

        ]

        street = streets[0] 
        day_period = "morning" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def object_detection4():
    try : 
        streets = [
          {
                "street_name": "Jl. Kawi Arah Barat (BRI Kawi)",
                "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/244729190133053856685781.m3u8?token=null",
                "start_x": 422,
                "start_y": 371,
                "end_x": 847,
                "end_y": 272
            }
        ]

        street = streets[0] 
        day_period = "afternoon" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def object_detection5():
    try : 
        streets = [
            {
                    "street_name": "Jl. Kawi Arah Timur (BRI Kawi)",
                    "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/269060901340905226381917.m3u8?token=null",
                    "start_x": 380,
                    "start_y": 410,
                    "end_x": 1000,
                    "end_y": 720
             }
        ]

        street = streets[0] 
        day_period = "afternoon" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
        
@shared_task
def object_detection6():
    try : 
        streets = [
        {
            "street_name": "Jl. Kawi Arah Utara (BRI Kawi)",
            "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/599118267175295987908194.m3u8?token=null",
            "start_x": 736,
            "start_y": 187,
            "end_x": 1033,
            "end_y":202
        }
        ]

        street = streets[0] 
        day_period = "afternoon" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration)
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def object_detection7():
    try : 
        streets = [
          {
            "street_name": "Jl. Kawi Arah Barat (BRI Kawi)",
            "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/244729190133053856685781.m3u8?token=null",
            "start_x": 422,
            "start_y": 371,
            "end_x": 847,
            "end_y": 272
        }
        ]

        street = streets[0] 
        day_period = "night" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def object_detection8():
    try : 
        streets = [
         {
                "street_name": "Jl. Kawi Arah Timur (BRI Kawi)",
                "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/269060901340905226381917.m3u8?token=null",
                "start_x": 380,
                "start_y": 410,
                "end_x": 1000,
                "end_y": 720
            }
        ]

        street = streets[0] 
        day_period = "night" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600# in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def object_detection9():
    try : 
        streets = [
        {
            "street_name": "Jl. Kawi Arah Utara (BRI Kawi)",
            "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/599118267175295987908194.m3u8?token=null",
            "start_x": 736,
            "start_y": 187,
            "end_x": 1033,
            "end_y":202
        }
        ]

        street = streets[0] 
        day_period = "night" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 3600 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)
    
@shared_task
def testing():
    try : 
        streets = [
        {
            "street_name": "Jl. Kawi Arah Utara (BRI Kawi)",
            "stream_url": "http://stream.cctv.malangkota.go.id/WebRTCApp/streams/599118267175295987908194.m3u8?token=null",
            "start_x": 736,
            "start_y": 187,
            "end_x": 1033,
            "end_y":202
        }
        ]

        street = streets[0] 
        day_period = "night" # should be 'morning' / 'afternoon' / 'night'
        date = datetime.today().strftime('%Y-%m-%d')
        duration = 10 # in seconds

        result = record_and_annotate_vehicles(street=street, day_period=day_period, date=date, recording_duration=duration, annotated_dir="static/result")
        logger.info(result)
        today = datetime.today().date()

        for i in result :
            if i["type"] == "car":
                jenis = "Mobil"
            else :
                jenis = "Motor"
            JumlahKendaraan.objects.create(
                                    jalan=i['street'],
                                    jam=i["time"],
                                    jenis=jenis,
                                    jumlah=i["count"],
                                    tanggal=i["date"],
                                    path_video=i["annotated_result_path"]
                                    )
                
        return "save to Database"

    except Exception as e:
        logger.error(f"Error saving to database: {e}")
        return str(e)