import pytest
from app import greet, untested_logic, bad_style
from bad_code import (
    calculate_area,
    unused_feature,
    duplicate_block,
    duplicate_block_2,
    delete_files,
)

def test_greet():
    assert greet("Test") == "Hello, Test!"

def test_untested_logic():
    assert untested_logic() == 200

def test_bad_style(monkeypatch, capsys):
    monkeypatch.setattr("builtins.eval", lambda x: 3)  # eval 우회
    bad_style()
    captured = capsys.readouterr()
    assert "This should not be here" in captured.out

def test_calculate_area():
    assert calculate_area(3, 4) == 12

def test_unused_feature(capsys):
    unused_feature()
    captured = capsys.readouterr()
    assert "Final:" in captured.out

def test_duplicate_block(capsys):
    duplicate_block()
    captured = capsys.readouterr()
    assert "block A" in captured.out

def test_duplicate_block_2(capsys):
    duplicate_block_2()
    captured = capsys.readouterr()
    assert "block F" in captured.out

def test_delete_files(monkeypatch):
    monkeypatch.setattr("os.system", lambda x: None)  # 실제 실행 방지
    delete_files()
