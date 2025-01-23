![Kyo's Django Ninja Tutorial](https://i.imgur.com/5WLyxcH.png)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-blue?labelColor=444&logo=pre-commit)](https://github.com/pre-commit/pre-commit)
[![linting - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![code style - Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/format.json?labelColor=444)](https://github.com/astral-sh/ruff)
[![Python](https://img.shields.io/badge/python-3.12-blue?labelColor=444&logo=python&logoColor=DDD)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-4.2-forestgreen?labelColor=444&logo=django)](https://www.djangoproject.com/)
[![Django Ninja](https://img.shields.io/badge/django--ninja-1.3-forestgreen?labelColor=444&&logoColor=DDD)](https://django-ninja.dev/)

# Django Ninja 系列教學

賀！本系列榮獲 Python 組「**優選**」獎 🏆（[得獎名單](https://ithelp.ithome.com.tw/2024ironman/reward)）

[2024 iThome 鐵人賽](https://ithelp.ithome.com.tw/2024ironman/)參賽作品：《[Django 忍法帖——Django Ninja 入門指南](https://ithelp.ithome.com.tw/users/20167825/ironman/7451)》

面向初學者的 Django Ninja 系列教學，旨在幫助你學習 Django Ninja，建立高效且現代的 API。

透過**範例專案**和 **30 篇文章**，你將逐步掌握 Django Ninja 的核心概念與使用方法，並了解它和 Django REST framework 的主要差異。

每個章節均包含具體的程式碼範例，讓你能**邊看邊學**，化理論為實踐。

> [!NOTE]
> 如果你對 Django 教學與 Python 開發文章感興趣，歡迎參考我的姐妹倉庫：[Django-Tutorial](https://github.com/kyomind/Django-Tutorial)。

## 第一章：導讀與 Django Ninja 介紹

- [卷 1：系列導讀 × 目標讀者](https://blog.kyomind.tw/django-ninja-01/)
- [卷 2：架構與章節導覽](https://blog.kyomind.tw/django-ninja-02/)
- [卷 3：Django Ninja 介紹——與 Django REST framework 主要區別](https://blog.kyomind.tw/django-ninja-03/)

## 第二章：範例專案與環境設定

- [卷 4：API 範例專案介紹](https://blog.kyomind.tw/django-ninja-04/)
- [卷 5：Python 現代開發工具介紹](https://blog.kyomind.tw/django-ninja-05/)
- [卷 6：環境設定 × 如何使用本專案](https://blog.kyomind.tw/django-ninja-06/)

## 第三章：Django Ninja 基本功

### 第一節：路由（Routers）

- [卷 7：路由（上）傳統 Django 路由做法](https://blog.kyomind.tw/django-ninja-07/)
- [卷 8：路由（下）Django Ninja 路由設定](https://blog.kyomind.tw/django-ninja-08/)

### 第二節：請求（HTTP Request）

- [卷 9：請求（一）Django Ninja 處理 HTTP 請求](https://blog.kyomind.tw/django-ninja-09/)
- [卷 10：請求（二）路徑參數 - Path Parameters](https://blog.kyomind.tw/django-ninja-10/)
- [卷 11：請求（三）查詢參數 - Query Parameters](https://blog.kyomind.tw/django-ninja-11/)
- [卷 12：請求（四）Request Body 與 Schema 介紹](https://blog.kyomind.tw/django-ninja-12/)

### 第三節：回應（HTTP Response）

- [卷 13：回應（一）Django Ninja 處理 HTTP 回應](https://blog.kyomind.tw/django-ninja-13/)
- [卷 14：回應（二）用 Schema 建立巢狀結構回應](https://blog.kyomind.tw/django-ninja-14/)
- [卷 15：回應（三）為何不用 ModelSchema？——相比 DRF，我更偏愛 Django Ninja 的理由](https://blog.kyomind.tw/django-ninja-15/)
- [卷 16：回應（四）Resolver 方法——欄位資料格式化](https://blog.kyomind.tw/django-ninja-16/)

## 第四章：API 文件

- [卷 17：API 文件（上）Django Ninja 文件實踐指南](https://blog.kyomind.tw/django-ninja-17/)
- [卷 18：API 文件（下）Pydantic Field 設定範例與預設值](https://blog.kyomind.tw/django-ninja-18/)

## 第五章：資料驗證與錯誤處理

- [卷 19：資料驗證（上）Pydantic 單一欄位驗證](https://blog.kyomind.tw/django-ninja-19/)
- [卷 20：資料驗證（下）Pydantic 跨欄位驗證](https://blog.kyomind.tw/django-ninja-20/)
- [卷 21：錯誤處理（上）HttpError 與自定義 HTTP 回應](https://blog.kyomind.tw/django-ninja-21/)
- [卷 22：錯誤處理（下）全域錯誤處理——使用 Exception Handlers](https://blog.kyomind.tw/django-ninja-22/)

## 第六章，API 進階功能
- [卷 23：檔案上傳——Django UploadedFile 介紹](https://blog.kyomind.tw/django-ninja-23/)
- [卷 24：分頁（上）Django Ninja 的內建分頁器](https://blog.kyomind.tw/django-ninja-24/)
- [卷 25：分頁（下）自定義分頁類別](https://blog.kyomind.tw/django-ninja-25/)
- [卷 26：資料查詢與過濾（上）FilterSchema 介紹](https://blog.kyomind.tw/django-ninja-26/)
- [卷 27：資料查詢與過濾（下）FilterSchema 多欄位查詢](https://blog.kyomind.tw/django-ninja-27/)

## 第七章：身分認證與單元測試

- [卷 28：身分認證——Session 認證與全域設定](https://blog.kyomind.tw/django-ninja-28/)
- [卷 29：單元測試——使用 Test Client 與 pytest 測試 API](https://blog.kyomind.tw/django-ninja-29/)

## 第八章：系列回顧與完賽心得

- [卷 30：系列回顧與完賽心得](https://blog.kyomind.tw/django-ninja-30/)
