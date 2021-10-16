package com.finance.data.entity;

import lombok.*;

import javax.persistence.*;
import javax.validation.constraints.NotBlank;
import javax.validation.constraints.NotNull;
import javax.validation.constraints.Size;
import java.util.Date;

@Entity @Table(name = "exchange_rate")
@NoArgsConstructor @AllArgsConstructor @Builder
@Setter @Getter @ToString
public class ExchangeRate {

    @Id
    @GeneratedValue(strategy = GenerationType.SEQUENCE)
    @Column(name = "exchange_rate_seq")
    private long exchangeRateSeq;

    @NotBlank
    @Size(min = 3, max = 3)
    @Column(name = "currency_code")
    private String currencyCode;

    @NotNull
    @Column(name = "currency_price")
    private double currencyPrice;

    @Column(name = "standard_date")
    private Date standardDate;

    @Column(name = "update_date")
    private Date updateDate;

    @NotBlank
    @Column(name = "from_data")
    private String fromData;

    @NotNull
    @Transient
    private long timestamp;
}
