package com.finance.data.service;

import com.finance.data.entity.KoreaStock;
import com.finance.data.repository.KoreaStockRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.Locale;

@Service
public class KoreaStockService {

    @Autowired
    private KoreaStockRepository koreaStockRepository;

    public KoreaStock saveKoreaStock(KoreaStock koreaStock) {
        KoreaStock newKoreaStock = KoreaStock.builder()
                .stockCode(koreaStock.getStockCode().toUpperCase(Locale.ROOT))
                .stockPrice(koreaStock.getStockPrice())
                .fromData(koreaStock.getFromData())
                .standardDate(new Date(koreaStock.getTimestamp()*1000L))
                .updateDate(new Date())
                .build();
        return koreaStockRepository.save(newKoreaStock);
    }
}
